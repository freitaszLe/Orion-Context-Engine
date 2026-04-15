import ollama
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client
from app.core.config import HOST_OLLAMA, MODELO_LLAMA, PROMPT_SISTEMA_ORION
from app.service.audit_service import registrar_auditoria

async def interagir_com_ia(mensagem_usuario: str) -> str:
    rastro = {
        "usuario_input": mensagem_usuario,
        "decisoes_ia": [],
        "respostas_backend": [],
        "resposta_final": ""
    }

    # 1. Abre a conexão SSE com o Servidor MCP
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            mcp_tools = await session.list_tools()

            # 2. Formata as ferramentas para o Ollama 
            tools_llama = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.inputSchema
                    }
                } for t in mcp_tools.tools
            ]

            mensagens_chat = [
                {"role": "system", "content": PROMPT_SISTEMA_ORION},
                {"role": "user", "content": mensagem_usuario}
            ]

            # === Usa o cliente Assíncrono ===
            async_ollama = ollama.AsyncClient(host=HOST_OLLAMA)
            
            # Primeira chamada (IA decide o que fazer)
            resposta = await async_ollama.chat(
                model=MODELO_LLAMA, 
                messages=mensagens_chat, 
                tools=tools_llama
            )
            mensagens_chat.append(resposta['message'])

            # 3. Execução de ferramentas via MCP
            if resposta['message'].get('tool_calls'):
                for tool in resposta['message']['tool_calls']:
                    nome_f = tool['function']['name']
                    args_f = tool['function']['arguments']

                    rastro["decisoes_ia"].append({"tool": nome_f, "args": args_f})

                    # Chama o servidor MCP e aguarda o resultado
                    resultado_mcp = await session.call_tool(nome_f, args_f)
                    
                    # O MCP retorna uma lista. Pegamos o texto do primeiro item.
                    texto_resultado = resultado_mcp.content[0].text if resultado_mcp.content else "{}"
                    
                    rastro["respostas_backend"].append(texto_resultado)

                    mensagens_chat.append({
                        "role": "tool",
                        "content": texto_resultado,
                        "name": nome_f
                    })

                # Segunda chamada: IA humaniza os dados retornados
                resposta_final = await async_ollama.chat(model=MODELO_LLAMA, messages=mensagens_chat)
                rastro["resposta_final"] = resposta_final['message']['content']
            else:
                rastro["resposta_final"] = resposta['message']['content']

            # 4. Finaliza a Auditoria e retorna
            registrar_auditoria(rastro)
            return rastro["resposta_final"]
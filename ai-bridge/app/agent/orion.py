import ollama
from app.core.config import HOST_OLLAMA, MODELO_LLAMA, PROMPT_SISTEMA_ORION
from app.tools.xsig_tools import consultar_bolsista_no_java, cadastrar_edital, listar_bolsistas, listar_editais, vincular_bolsista_no_edital

cliente_llama = ollama.Client(host=HOST_OLLAMA)

# Dicionário de ferramentas
ferramentas_disponiveis = {
    "consultar_bolsista_no_java": consultar_bolsista_no_java,
    "cadastrar_edital": cadastrar_edital,
    "listar_bolsistas": listar_bolsistas,
    "listar_editais": listar_editais,
    "vincular_bolsista_no_edital": vincular_bolsista_no_edital
}

def interagir_com_ia(mensagem_usuario: str) -> str:
    mensagens_chat = [
        {"role": "system", "content": PROMPT_SISTEMA_ORION},
        {"role": "user", "content": mensagem_usuario}
    ]

    print("\n🧠 [IA] Enviando pergunta para o Llama 3.1 no laboratório...")
    
    # 3. Adicione a função na lista 'tools' aqui:
    resposta_ia = cliente_llama.chat(
        model=MODELO_LLAMA,
        messages=mensagens_chat,
        tools=[consultar_bolsista_no_java, cadastrar_edital, listar_bolsistas, listar_editais, vincular_bolsista_no_edital]
    )

    mensagens_chat.append(resposta_ia['message'])

    # 2. Se não tem ferramentas, responde direto (Bate-papo normal)
    if not resposta_ia['message'].get('tool_calls'):
        print("🗣️ [IA] Llama respondeu diretamente (sem usar ferramentas).")
        return resposta_ia['message']['content']

    # 3. Se pediu ferramenta, o Python executa (Ação)
    for tool in resposta_ia['message']['tool_calls']:
        nome_funcao = tool['function']['name']
        argumentos = tool['function']['arguments']
        
        if nome_funcao in ferramentas_disponiveis:
            funcao_python = ferramentas_disponiveis[nome_funcao]
            resultado_ferramenta = funcao_python(**argumentos)
            
            # Salva o resultado no histórico
            mensagens_chat.append({
                "role": "tool",
                "content": str(resultado_ferramenta),
                "name": nome_funcao
            })

    # 4. IA lê o resultado e formula a resposta humanizada
    print("🗣️ [IA] Llama leu os dados do Java e está gerando a resposta final...")
    resposta_final = cliente_llama.chat(model=MODELO_LLAMA, messages=mensagens_chat)
    
    return resposta_final['message']['content']
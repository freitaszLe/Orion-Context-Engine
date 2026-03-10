from mcp.server.fastmcp import FastMCP
import requests
import json

# 1. Inicializamos o Servidor MCP
mcp = FastMCP("mini-xsig-mcp")

# 2. Criamos a Tool que agora consome a API real!
@mcp.tool()
def consultar_bolsista(id_bolsista: str) -> str:
    """Consulta o status e o IRA de um bolsista no sistema X-SIG usando o ID numérico."""
    
    # A URL da sua API Java rodando localmente na porta 8081
    url = f"http://localhost:8081/api/bolsistas/{id_bolsista}"
    
    try:
        # O Python bate na porta do Java e pede os dados
        response = requests.get(url)
        
        # Se o Spring Boot retornar 200 OK (Encontrou o aluno)
        if response.status_code == 200:
            aluno = response.json()
            return json.dumps(aluno, ensure_ascii=False, indent=2)
        
        # Se o Spring Boot retornar 404 Not Found (Não encontrou)
        elif response.status_code == 404:
            return f"Erro: Bolsista com ID {id_bolsista} não encontrado no banco de dados do X-SIG."
        
        # Outros erros (ex: erro no código Java)
        else:
            return f"Erro de comunicação com a API X-SIG. Código HTTP: {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        # Se você esquecer de dar o 'Run' no IntelliJ, a IA avisa!
        return f"Erro crítico: O servidor Java do X-SIG parece estar desligado. Verifique a porta 8081."

# 3. Rodamos o servidor
if __name__ == "__main__":
    mcp.run()
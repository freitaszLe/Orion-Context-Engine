from fastmcp import FastMCP
import requests
import os
from app.core.config import URL_BASE_JAVA

# 1. Inicializa o Servidor MCP
mcp = FastMCP("Orion-XSIG-Server")

# --- FERRAMENTAS (Tools) ---

@mcp.tool()
def listar_bolsistas() -> list:
    """
    Lista todos os bolsistas cadastrados no X-SIG da FAPEMAT.
    DICA PARA A IA: Use esta ferramenta OBRIGATORIAMENTE para buscar 
    o 'id' numérico de um bolsista quando o usuário fornecer apenas o nome.
    """
    try:
        r = requests.get(f"{URL_BASE_JAVA}/bolsistas", timeout=5)
        return r.json() if r.status_code == 200 else []
    except:
        return [{"erro": "Core-API Java offline"}]
    
@mcp.tool()
def consultar_bolsista(id_bolsista: int) -> dict:
    """Consulta os detalhes técnicos de um bolsista específico pelo ID."""
    try:
        r = requests.get(f"{URL_BASE_JAVA}/bolsistas/{id_bolsista}", timeout=5)
        return r.json() if r.status_code == 200 else {"erro": "Não encontrado"}
    except:
        return {"erro": "Erro de conexão"}

@mcp.tool()
def listar_editais() -> list:
    """
    Lista todos os editais disponíveis e cadastrados no sistema.
    DICA PARA A IA: Use esta ferramenta OBRIGATORIAMENTE para buscar 
    o 'id' numérico de um edital quando o usuário fornecer apenas o título ou o número (ex: 02/2026).
    """
    try:
        r = requests.get(f"{URL_BASE_JAVA}/editais", timeout=5)
        return r.json() if r.status_code == 200 else []
    except:
        return [{"erro": "Core-API Java offline"}]

@mcp.tool()
def cadastrar_edital(titulo: str, numero: str, data_fim_inscricao: str, 
                     ira_minimo: float, permite_clt: bool) -> dict:
    """
    Cadastra um novo edital no banco de dados Java.
    O formato da data deve ser YYYY-MM-DD.
    """
    payload = {
        "numero": numero,
        "titulo": titulo,
        "iraMinimo": ira_minimo,
        "permiteClt": permite_clt,
        "dataFimInscricao": data_fim_inscricao
    }
    try:
        r = requests.post(f"{URL_BASE_JAVA}/editais", json=payload, timeout=5)
        return r.json() if r.status_code in [200, 201] else {"erro": r.text}
    except:
        return {"erro": "Falha ao cadastrar edital"}

@mcp.tool()
def vincular_bolsista_edital(id_bolsista: int, id_edital: int) -> dict:
    """
    Vincula um bolsista a um edital no banco de dados.
    
    ATENÇÃO CRÍTICA PARA A IA: 
    - Os parâmetros id_bolsista e id_edital SÃO ESTRITAMENTE NÚMEROS INTEIROS (ex: 1, 2, 3).
    - NUNCA repasse strings, nomes (ex: 'Maria') ou números formatados (ex: '02/2026') para esta ferramenta.
    - Se você não tem os IDs inteiros exatos em mãos, chame listar_bolsistas() e listar_editais() primeiro para encontrá-los.
    """
    try:
        r = requests.post(f"{URL_BASE_JAVA}/editais/vincular/{id_bolsista}/{id_edital}", timeout=5)
        if r.status_code in [200, 201]:
            return r.json()
        return {"erro_negocio": r.json() if r.status_code == 400 else f"Erro {r.status_code}"}
    except:
        return {"erro_infra": "Servidor Java offline"}

# --- RECURSOS (Resources) ---
@mcp.resource("audit://logs/latest")
def get_latest_audit_log() -> str:
    """Recupera o conteúdo do último rastro de execução gerado."""
    log_dir = "logs/auditoria"
    try:
        arquivos = sorted(os.listdir(log_dir), reverse=True)
        if not arquivos: return "Nenhum log disponível."
        with open(f"{log_dir}/{arquivos[0]}", 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Erro ao acessar logs de auditoria."

if __name__ == "__main__":
    # Rodando como servidor HTTP (transporte SSE) para o orion.py conectar via rede
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
from mcp.server.fastmcp import FastMCP
from app.tools.xsig_tools import (
    listar_bolsistas,
    consultar_bolsista_no_java,
    listar_editais,
    cadastrar_edital,
    vincular_bolsista_no_edital,
)

mcp = FastMCP("Orion X-SIG Server")

@mcp.tool()
def listar_todos_bolsistas() -> list:
    """Lista todos os bolsistas cadastrados no sistema X-SIG da FAPEMAT."""
    return listar_bolsistas()

@mcp.tool()
def consultar_bolsista(id_bolsista: int) -> dict:
    """Consulta os detalhes de um bolsista pelo ID."""
    return consultar_bolsista_no_java(id_bolsista)

@mcp.tool()
def listar_todos_editais() -> list:
    """Lista todos os editais disponíveis no sistema."""
    return listar_editais()

@mcp.tool()
def criar_edital(
    titulo: str,
    numero: str,
    data_fim_inscricao: str,
    ira_minimo: float,
    permite_clt: bool
) -> dict:
    """
    Cadastra um novo edital no sistema.
    data_fim_inscricao deve estar no formato YYYY-MM-DD.
    """
    return cadastrar_edital(titulo, numero, data_fim_inscricao, ira_minimo, permite_clt)

@mcp.tool()
def vincular_bolsista_edital(id_bolsista: int, id_edital: int) -> dict:
    """
    Vincula um bolsista a um edital. Verifica regras de negócio automaticamente.
    Retorna erro_negocio se as regras não forem atendidas (IRA mínimo, CLT, etc).
    """
    return vincular_bolsista_no_edital(id_bolsista, id_edital)


if __name__ == "__main__":
    mcp.run()  # roda via stdio — padrão para Claude Desktop
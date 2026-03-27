import requests
from app.core.config import URL_BASE_JAVA 

def listar_bolsistas() -> list:
    """Lista todos os bolsistas cadastrados no sistema. Use esta ferramenta quando o usuário quiser saber a quantidade total de bolsistas ou quem são eles."""
    print("\n⚙️ [Ferramenta] O Llama pediu para listar TODOS os bolsistas...")
    try:
        r = requests.get(f"{URL_BASE_JAVA}/bolsistas")
        return r.json() if r.status_code == 200 else [{"erro": f"Status {r.status_code}"}]
    except:
        return [{"erro": "O servidor Java está desligado."}]

def consultar_bolsista_no_java(id_bolsista: int) -> dict:
    """Consulta os detalhes de um bolsista no banco de dados Java usando o seu ID."""
    print(f"\n⚙️ [Ferramenta] O Llama pediu para consultar o bolsista {id_bolsista}...")
    try:
        r = requests.get(f"{URL_BASE_JAVA}/bolsistas/{id_bolsista}")
        return r.json() if r.status_code == 200 else {"erro": f"Bolsista {id_bolsista} não encontrado."}
    except:
        return {"erro": "O servidor Java está desligado."}

def cadastrar_edital(titulo: str, numero: str, data_fim_inscricao: str, ira_minimo: float, permite_clt: bool) -> dict:
    """Cadastra um novo edital no banco de dados Java."""
    # Como não temos o endpoint no Java ainda, vamos simular a resposta
    print(f"\n⚙️ [Ferramenta Simulada] O Llama tentou cadastrar edital: {titulo}...")
    # Retornamos um mock com o ID simulado para a IA poder confirmar
    return {"id_gerado": 999, "titulo": titulo, "data_fim_inscricao": data_fim_inscricao, "mensagem": "Simulação de sucesso!"}
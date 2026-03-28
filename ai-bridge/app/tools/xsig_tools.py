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

def listar_editais() -> list:
    """Lista todos os editais disponíveis e cadastrados no sistema. Use esta ferramenta quando o usuário pedir para listar, ver ou buscar editais."""
    print("\n⚙️ [Ferramenta] O Llama pediu para listar TODOS os editais no Java...")
    try:
        r = requests.get(f"{URL_BASE_JAVA}/editais")
        return r.json() if r.status_code == 200 else [{"erro": f"Status {r.status_code}"}]
    except:
        return [{"erro": "O servidor Java está desligado."}]

def cadastrar_edital(titulo: str, numero: str, data_fim_inscricao: str, ira_minimo: float, permite_clt: bool) -> dict:
    """Cadastra um novo edital no banco de dados Java."""
    print(f"\n⚙️ [Ferramenta] O Llama está cadastrando o edital: {titulo} no Java...")
    
    # Montando o JSON
    payload = {
        "numero": numero,
        "titulo": titulo,
        "iraMinimo": ira_minimo,
        "permiteClt": permite_clt,
        "dataFimInscricao": data_fim_inscricao
    }
    
    try:
        r = requests.post(f"{URL_BASE_JAVA}/editais", json=payload)
        return r.json() if r.status_code in [200, 201] else {"erro": f"Falha ao cadastrar: {r.text}"}
    except:
        return {"erro": "O servidor Java está desligado."}

def vincular_bolsista_no_edital(id_bolsista: int, id_edital: int) -> dict:
    """
    Tenta vincular um bolsista ao edital no backend.
    IMPORTANTE PARA A IA: Se esta ferramenta retornar um "erro_negocio", 
    você DEVE explicar o motivo exato para o usuário de forma amigável.
    """
    try:
        r = requests.post(f"{URL_BASE_JAVA}/editais/vincular/{id_bolsista}/{id_edital}")
        
        # Se deu 200/201, sucesso!
        if r.status_code in [200, 201]:
            return r.json()
            
        # Se deu 400 (Regra de negócio barrada no Java)
        if r.status_code == 400:
            # O Python não sabe qual é a regra, ele só repassa a fofoca!
            return {"erro_negocio": r.json()}
            
    except Exception as e:
        return {"erro_infra": "O servidor Java está desligado."}
    
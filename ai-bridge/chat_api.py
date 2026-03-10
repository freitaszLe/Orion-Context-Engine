import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

# 1. Configuração da API
CHAVE_API = "AIzaSyCDbrjr41cZgUoBIJesZELnISyBiTd-xpg"
client = genai.Client(api_key=CHAVE_API)

URL_BASE = "http://localhost:8081/api"

# =======================================================
# 2. DEFININDO AS FERRAMENTAS (TOOLS) PARA O GEMINI
# =======================================================

def consultar_bolsista_no_java(id_bolsista: int) -> dict:
    """Consulta os dados de um bolsista no banco de dados do X-SIG usando o seu ID."""
    try:
        r = requests.get(f"{URL_BASE}/bolsistas/{id_bolsista}")
        return r.json() if r.status_code == 200 else {"erro": f"Status {r.status_code}"}
    except:
        return {"erro": "O servidor Java está desligado."}

def listar_editais() -> list:
    """Lista todos os editais disponíveis no sistema."""
    try:
        r = requests.get(f"{URL_BASE}/editais")
        return r.json() if r.status_code == 200 else [{"erro": f"Status {r.status_code}"}]
    except:
        return [{"erro": "O servidor Java está desligado."}]

def cadastrar_edital(numero: str, titulo: str, ira_minimo: float, permite_clt: bool, data_fim_inscricao: str) -> dict:
    """Cadastra um novo edital. O campo data_fim_inscricao deve estar estritamente no formato YYYY-MM-DD."""
    payload = {
        "numero": numero,
        "titulo": titulo,
        "iraMinimo": ira_minimo,
        "permiteClt": permite_clt,
        "dataFimInscricao": data_fim_inscricao
    }
    try:
        r = requests.post(f"{URL_BASE}/editais", json=payload)
        return r.json() if r.status_code == 200 else {"erro": f"Erro {r.status_code}"}
    except:
        return {"erro": "O servidor Java está desligado."}

def listar_bolsistas() -> list:
    """Lista todos os bolsistas cadastrados no sistema."""
    try:
        r = requests.get(f"{URL_BASE}/bolsistas")
        return r.json() if r.status_code == 200 else [{"erro": f"Status {r.status_code}"}]
    except:
        return [{"erro": "O servidor Java está desligado."}]

def cadastrar_bolsista(nome: str, ira: float, vinculo: str, status: str, edital_id: int) -> dict:
    """Cadastra um novo bolsista e o vincula a um edital existente através do ID do edital."""
    payload = {
        "nome": nome,
        "ira": ira,
        "vinculo": vinculo,
        "status": status,
        "edital": {"id": edital_id} # É assim que o Spring Boot entende o relacionamento!
    }
    try:
        r = requests.post(f"{URL_BASE}/bolsistas", json=payload)
        return r.json() if r.status_code == 200 else {"erro": f"Erro {r.status_code}"}
    except:
        return {"erro": "O servidor Java está desligado."}

# =======================================================
# 3. INICIALIZANDO O CÉREBRO COM TODAS AS FERRAMENTAS
# =======================================================
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        # Passamos a lista inteira de ferramentas para a IA usar como quiser!
        tools=[consultar_bolsista_no_java, listar_editais, cadastrar_edital, listar_bolsistas, cadastrar_bolsista],
        system_instruction="Você é o assistente virtual do sistema X-SIG da FAPEMAT. Você pode listar, consultar e cadastrar tanto bolsistas quanto editais. Quando listar dados, formate de um jeito bonito usando Markdown e negritos."
    )
)

# =======================================================
# 4. ROTA DO FASTAPI (A PONTE COM O ANGULAR)
# =======================================================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mensagem(BaseModel):
    texto: str

@app.post("/api/chat")
def processar_chat(msg: Mensagem):
    try:
        resposta_ia = chat.send_message(msg.texto)
        return {"mensagem": resposta_ia.text}
    except Exception as e:
        return {"mensagem": f"Ops, erro de comunicação com a IA: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import APIRouter, HTTPException
from app.core.models import Mensagem
from app.agent.orion import interagir_com_ia

router = APIRouter()

@router.post("/chat")
def processar_chat(msg: Mensagem):
    try:
        resposta_texto = interagir_com_ia(msg.texto)
        return {"mensagem": resposta_texto}
    except Exception as e:
        print(f"❌ Erro na comunicação com a IA: {e}")
        raise HTTPException(status_code=500, detail="Erro interno no servidor da IA")
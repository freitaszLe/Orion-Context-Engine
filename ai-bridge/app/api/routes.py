from fastapi import APIRouter, HTTPException
from app.core.models import Mensagem
from app.agent.orion import interagir_com_ia
import traceback # Para ver o erro real no terminal

router = APIRouter()

@router.post("/chat")
async def processar_chat(msg: Mensagem):
    try:
        # Chama o agente assíncrono
        resposta_texto = await interagir_com_ia(msg.texto) 
        return {"mensagem": resposta_texto}
    
    except Exception as e:
        print("❌ ERRO NO FLUXO ORION/MCP:")
        traceback.print_exc() 
        
        raise HTTPException(
            status_code=500, 
            detail=f"Erro interno na orquestração: {str(e)}"
        )
    
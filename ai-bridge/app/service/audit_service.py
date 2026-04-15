import json
import os
from datetime import datetime

LOG_DIR = "logs/auditoria"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def registrar_auditoria(payload: dict):
    """Salva o rastro de execução em um arquivo JSON para auditoria futura."""
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{LOG_DIR}/interacao_{data_hora}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=4)
    
    print(f"📄 [Auditoria] Rastro de execução salvo em: {filename}")
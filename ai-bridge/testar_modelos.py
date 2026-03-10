import google.generativeai as genai

# Cole a sua chave real aqui, com aspas!
CHAVE_API = "AIzaSyCDbrjr41cZgUoBIJesZELnISyBiTd-xpg" 
genai.configure(api_key=CHAVE_API)

print("🔍 Buscando modelos disponíveis para a sua chave...\n")

# Pede para o Google listar tudo que você tem acesso
for m in genai.list_models():
    # Filtra só os modelos que servem para gerar texto/chat (generateContent)
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ Nome exato para usar: {m.name}")
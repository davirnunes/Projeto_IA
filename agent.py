import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Erro: Variável GEMINI_API_KEY não encontrada.")
    print("Verifique se você criou o arquivo .env corretamente!")
    exit()

client = genai.Client(api_key=api_key)

try:
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
except FileNotFoundError:
    print("Erro: Arquivo system_prompt.txt não encontrado.")
    exit()

config = types.GenerateContentConfig(
    system_instruction=system_prompt,
    temperature=0.5, 
)

print("🇬🇧 EngTutor iniciado! Let's practice! (Digite 'sair' para encerrar)\n")

chat = client.chats.create(model="gemini-2.5-flash", config=config)

while True:
    entrada = input("Você: ").strip()
    
    if entrada.lower() == "sair":
        print("EngTutor: See you later! Keep practicing.")
        break
    
    if not entrada:
        continue
        
    try:
        resposta = chat.send_message(entrada)
        print(f"\nEngTutor: {resposta.text}\n")
    except Exception as e:
        print(f"\nErro de comunicação com a API: {e}\n")
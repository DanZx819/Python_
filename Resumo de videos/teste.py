import whisper
import os 
import openai


os.chdir("C:\\Users\\Daniel\Desktop\\Estudos\\Python_\\Resumo de videos\\Audio")
modelo = whisper.load_model("base")

resposta = modelo.transcribe("audio1.mp3")
resumir = str(f"Resuma este texto para mim {resposta['text']}")
print(resumir)

chave_api = "sk-gABnK_tylcvGCl771B0k9N0mvX-1Fo5wM6cC9NgL9LT3BlbkFJaHWXAyOEBUzjnAtOda2PO-PiqP1Ln6KbCK-InqASsA"
openai.api_key = chave_api

# Substitua pela sua chave de API

def gerar_resposta(pergunta):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-3.5-turbo" se preferir
        messages=[
            {"role": "system", "content": "Você é i, assistente que Resume textos"},
            {"role": "user", "content": pergunta}
        ]
    )

    return response['choices'][0]['message']['content']

# Exemplo de uso
resposta = gerar_resposta(resumir)
print(resposta)


import openai
import whisper
import os
os.chdir("C:\\Users\\Daniel\Desktop\\Estudos\\Python_\\Resumo de videos\\Audio")
# Nova chave de API
openai.api_key = "sk-gABnK_tylcvGCl771B0k9N0mvX-1Fo5wM6cC9NgL9LT3BlbkFJaHWXAyOEBUzjnAtOda2PO-PiqP1Ln6KbCK-InqASsA"

modelo = whisper.load_model("base")
resposta = modelo.transcribe("Audio1.mp3")

# Monta o texto para ser resumido
resumir = f"Resuma este texto para mim: {resposta['text']}"

# Função para gerar resposta do ChatGPT
def gerar_resposta(pergunta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-instruct",  # Ou "gpt-4", se disponível
            messages=[
                {"role": "system", "content": "Você é um assistente que resume textos."},
                {"role": "user", "content": pergunta}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
resposta_resumida = gerar_resposta(resumir)
print(resposta_resumida)

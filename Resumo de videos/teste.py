import fun
import os

De_pasta = os.chdir("C:\\Users\\Daniel\\Desktop\\Estudos\\Python_\\Resumo de videos\\")
arquivos = os.listdir()

for c in arquivos:
    if ".mp4" in c:
        arquivo_nome = c
        para_videos = os.chdir("C:\\Users\\Daniel\\Desktop\\Estudos\\Python_\\Resumo de videos\\Videos\\")
        videos = os.listdir()
        for v in videos:
            if v == arquivo_nome:
                os.remove(v)
                
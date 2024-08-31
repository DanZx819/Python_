
from pytubefix import YouTube
import os
from pathlib import Path
from moviepy.editor import *



def Baixar():
    link = input("Digite o link do video que voce deseja baixar: ")

    yt = YouTube(link)

    print("Baixando", yt.title)

    resolucao = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    resolucao.download()

    print("Download Concluido")

def Mudar_diretorio():
    De_pasta = os.chdir("C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos")

    arquivos = os.listdir()

    for arquivo in arquivos:
        if '.mp4' in arquivo:
            os.rename(arquivo, "C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos\\Videos\\" + arquivo)


def Conversor(path_list):

    for file in path_list:
        Video = VideoFileClip(str(file))
        Video.audio.write_audiofile(f"{str(file)}.mp3")

    directory_to_save = r"c:\\Users\daniz\\OneDrive\\Área de Trabalho\Area de Trabalho\\Estudos\\Python\\Resumo de videos\\Videos\\"

    path_list = Path(directory_to_save).glob("*.mp4")

def Mudar_diretorio_audio():
    os.chdir("C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos\\Videos")

    arquivos = os.listdir()

    for arquivo in arquivos:
        if '.mp3' in arquivo:
            os.rename(arquivo, "C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos\\Audio\\" + arquivo)


    
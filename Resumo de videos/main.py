import fun
import os
from pytubefix import YouTube

from pathlib import Path


os.chdir("C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos")

fun.Baixar()
fun.Mudar_diretorio()


path_list = Path("C:\\Users\\daniz\\OneDrive\\Área de Trabalho\\Area de Trabalho\\Estudos\\Python\\Resumo de videos\\Videos").glob("*.mp4")
fun.Conversor(path_list)
fun.Mudar_diretorio_audio()


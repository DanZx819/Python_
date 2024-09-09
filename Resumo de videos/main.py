import fun
import os
from pathlib import Path


os.chdir("C:\\Users\\Daniel\\Desktop\\Estudos\\Python_\\Resumo de videos")

fun.BaixarVideo()
fun.Mudar_diretorio()


path_list = Path("C:\\Users\\Daniel\\Desktop\\Estudos\\Python_\\Resumo de videos\\Videos").glob("*.mp4")
fun.Conversor(path_list)
fun.Mudar_diretorio_audio()


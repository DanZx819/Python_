import time
import random

print("O professor está sorteando a ordem da apresentação dos trabalhos")

nomes = ["Sofia", "Maria","Giulia","Julia"]
escolha = random.sample(nomes, k=4)
format = " ".join(escolha)

print(f"A ordem sera {format}.")

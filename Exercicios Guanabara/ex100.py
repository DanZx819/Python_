import random
import time

def sortear(lst):
    for c in range(0,5):
        lst.append(random.randint(0,10))
    print("Lista: ", end='')
    for c in lst:
        print(f"{c} ->", end=' ', flush=True)
        time.sleep(0.1)
    print("Fim da lista")

def somapar(lst):
    soma = 0
    nump = []
    for c in lst:
        if c % 2 == 0:
            nump.append(c)
            soma += c
    print("Lista dos números pares: ", end='')
    for c in nump:
        print(f"{c} ->", end=' ', flush=True)
        time.sleep(0.1)
    print("Fim da lista")
    print(f"A soma dos núeros pares foi = {soma}")





numeros = []
sortear(numeros)
somapar(numeros)
import time
import os

cadastro = {}
gols = []
cadastro['nome'] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas ele jogou: "))

for c in range(0, partidas):
    gols.append(int(input(f"Quantos gols ele fez na partida {c+1}:"))) 
total = 0
for g in gols:
    total += g

cadastro['gols'] = gols
cadastro['total'] = total
print('-='*30)
print(cadastro)
print('-='*30)

for c,v in cadastro.items():
    print(f"O campo {c} tem valor de {v}")
print('-='*30)

for n,a in cadastro.items():
    if n == 'nome':
        print(f"O jogador {a} jogou {partidas} partidas.")
    if n == 'gols':
        for k,l in enumerate(cadastro['gols']):
            print(f"    => Na partida {k+1} ele marcou {a[k]} gol.")
    if n == 'total':
        print(f"Total de {a} gols") 
print('-='*30)

time.sleep(5)

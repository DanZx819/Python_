import random
import time
import os
import operator
jogadas = {'jogador1': random.randint(1,6),
           'jogador2': random.randint(1,6),
           'jogador3': random.randint(1,6),
           'jogador4': random.randint(1,6)}

print("-="*15)
for j,v in jogadas.items():
    print(f"{j} = {v}")
    time.sleep(1)

organizado = sorted(jogadas.items(), key=operator.itemgetter(1), reverse=True)
print("-="*15)
print(" "*10, end='')
print("Ranking")

for i,v in enumerate(organizado):
    print(f"{i+1} Lugar -> {v[0]} = {v[1]}")
    time.sleep(1)
print("-="*15)

time.sleep(5)

os.system('cls')
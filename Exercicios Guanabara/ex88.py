import random

lista = []
temp = []
pergunta = int(input("Quantos jogos você deseja fazer: "))

for q in range(0, pergunta):
    while len(temp) < 5:
        comp = random.randint(1, 60)
        if comp not in temp:
            temp.append(comp)
    
    lista.append(temp[:])
    temp.clear()

print("-="*15)
for c,jogo in enumerate(lista):
    print(f"Jogo {c + 1}:{jogo}")

print("-="*15)
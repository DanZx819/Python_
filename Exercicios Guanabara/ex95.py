import os
time = []
jogador = {}
partidas = []

while True:#Buscando Jogador
    jogador.clear()
    jogador['nome'] = str(input("Nome: "))
    tot = int(input("Quantas partidas ele jogou: "))

    for c in range(0,tot):
        partidas.append(int(input(f"Quantos gols ele fez na partida {c+1}: "))) 
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas[:])
    partidas.clear()
    time.append(jogador.copy())
    
    pergunta = str(input("Você quer continuar [S/N]:")).upper()
    if pergunta == 'N':
        break

#Fazendo a tabela 
print("-="*30)
print("cod ", end='')
for i in jogador.keys():
    print(f"{str(i):<15}", end='')
print()
for I,v in enumerate(time):
    print(f"{I:<3}", end="")
    for d in v.values():
        print(f"{str(d):<15} ", end="")
    print()
print("-="*30)
#Buscando o Jogador especifico
while True:
    busca = int(input("Digite o cod do jogador desejado para buscar [999 sair]: "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Não existe jogador com este cod!!!")
    else:
        print("-="*30)
        print(f"Levantamento do Jogador {time[busca]['nome']}")
        for i,g in enumerate(time[busca]['gols']):
            print(f"Na partida {i+1} ele fez {g} gols")

            
os.system("cls")
            
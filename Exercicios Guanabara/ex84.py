lista = []
temp = []
maior = 0
menor = 0
while True:
    temp.append(str(input("Nome:")))
    temp.append(int(input("Peso:")))

    if len(lista) == 0:
        maior = temp[1]
        menor = temp [1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()

    pergunta = str(input("Você quer continuar [S/N]: "))
    if pergunta in 'Nn':
        break
print(f"{len(lista)} pessoas foram cadastradas")
print(f"Maior peso {maior}", end=' ')
for p in lista:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
print()
print(f"Menor peso {menor}", end=' ')
for p in lista:
    if p[1] == menor:
        print(f"{p[0]}", end=' ')

valores = []

while True:
    valor =  int(input("Digite um número:"))
    if valor not in valores:
        valores.append(valor)
    pergunta = str(input("Você quer continuar [S/N]: "))
    if pergunta in "Nn":
        break

valores.sort()
print("Valores da lista ->",end=' ')
for c in valores:
    print(f"{c}", end=' -> ')
print("Fim da lista")
    
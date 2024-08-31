lista = []

while True:
    valores = int(input("Digite um valor: "))
    lista.append(valores)
    pergunta = str(input("VocÊ quer digiter mais números [S/N]: "))
    if pergunta in "Nn":
        break
listapar = []
listaimpar = []
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)

print("Lista:", end="")

for y in lista:
    print(f"{y}", end=" ")
print("-> Fim da lista")

print("Lista Par:", end="")
for x in listapar:
    print(f"{x}", end=" ")
print("-> Fim da lista par")
print("Lista Impar:", end="")

for z in listaimpar:
    print(f"{z}", end = " ")
print("-> Fim da lista impar")


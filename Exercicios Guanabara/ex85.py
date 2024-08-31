

lista =[[],[]]
valor = 0
for c in range(0,7):
    valor = int(input("Digite um valor:"))
    if valor % 2 == 0:
        lista[1].append(valor)
    else:
        lista[0].append(valor)

lista[0].sort()
lista[1].sort()

print(f"Lista dos números Impares -> {lista[0]}")
print(f"Lista dos números Pares -> {lista[1]}")

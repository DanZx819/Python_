
cont = 0
soma = 0
n = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"Foram digitados {cont} números e a soma deles foi de {soma}.")
para = 0
n = 0
numeros = 0
cont = 0
n = int(input("Digite um numero: "))
while n != 999:
    para = numeros
    numeros += n
    cont += 1
    n = int(input("Digite um numero: "))

print(f"A soma dos numeros é igual a {numeros}, e foram digitados {cont} numeros.")
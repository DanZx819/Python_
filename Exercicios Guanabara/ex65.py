
maior = 0
menor = 0
cont = 0
cont2= 'S'
soma = 0
while cont2 == 'S':
    n = int(input("Digite um numero: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input("Você quer continuar? [S/N]\n"))
    if continuar in 'Nn':
        cont2 = 'N'


print(f"O maior numero digitado foi {maior} e o menor foi {menor} e a média de todos os numeros digitados foi {soma / cont} ")

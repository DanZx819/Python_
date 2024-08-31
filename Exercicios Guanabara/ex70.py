nome = ''
nomebar = ''
preço = 0
preçotot = 0
maior1000 = 0
menor = 0
cont = 0
while True:
    nome = str(input("Qual o nome do produto: ")).strip()
    preço = float(input("Qual o preço do produto: "))
    cont += 1
    preçotot += preço
    if preço > 1000:
        maior1000 += 1
    if  cont == 1:
        menor = preço
        nomebar = nome
    else:
        if preço < menor:
            menor = preço
            nomebar = nome
    continuar = str(input("Você quer continuar [S/N]: ")).strip()
    if continuar in 'Nn':
        print("*"*40)
        print(f"O total gasto foi de R${preçotot}.")
        print(f"O nome do produto mais barato é {nomebar}!")
        print(f'A quantidade de produtos que custam mais de R$1000 é {maior1000}.')
        break

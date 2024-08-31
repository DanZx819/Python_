cadastro = {}
lista = []
idade = []
lista_mulher = []
while True:
    cadastro['nome'] = str(input("Nome: "))
    while True:
        cadastro['Sexo'] = str(input("Sexo [M/F]: ")).upper()
        if cadastro['Sexo'] in 'MF':
            break
        else:
            print("Digite M para masculino ou F para Feminino.")
    if cadastro['Sexo'] == 'F':
        lista_mulher.append(cadastro['nome'])
    while True:
        cadastro['idade'] = int(input("Idade: "))
        if cadastro['idade'] > 0:
            break
        else:
            print('Digite uma idade maior que 0!')
    idade.append(cadastro['idade'])
    lista.append(cadastro)
    del cadastro
    cadastro = {}
    pergunta = str(input("Você quer continuar [S/N]: ")).upper().strip()

    if pergunta in 'N':
        break
total = 0
for c in idade:
   total += c
   média = total / len(lista)
print("-="*15)
print(f'(A)-Foram cadastradas {len(lista)} pessoas.')
print(f"(B)-A média das idade foi de {média}")
print(f"(C)-As mulheres cadastradas foram", end=' ')
for l in lista_mulher:
    print(f"{l}", end=' ')
print()
print(f"(D)-Lista das pessoas acima da média:", end='')
for p in lista:
    if p['idade'] >= média:
        print("     ")
        for v,k in p.items():
            print(f"{v} = {k}; ", end='')  
print()
print("     >>Encerrado<<       ")
print("-="*15)
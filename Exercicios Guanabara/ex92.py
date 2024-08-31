from datetime import datetime


cadastro ={}
cadastro['Nome'] = str(input("Nome: "))
ano = int(input("Data de nascimento: "))
idade = datetime.now().year - ano
cadastro['idade'] = idade

while True:
    cadastro['CDT'] = int(input("Carteira de Trabalho [0 não tem]: "))
    if cadastro['CDT'] == 0:
        break
    else:
        cadastro['Ano da Contratação'] = int(input("Ano da contratação: "))
        cadastro['Salario'] = float(input("Salario: "))
        cadastro['Aposentadoria'] = (cadastro['idade'] + cadastro['Ano da Contratação'] + 35) - datetime.now().year
        break


print("-="*30)
if cadastro['CDT'] == 0:
    for c,v in cadastro.items():
        print(f"{c} tem o valor de {v}")
else:
    for c,v in cadastro.items():
        print(f"{c} tem o valor de {v}")

print("-="*30)
dic = {}
dic['nome'] = str(input("Nome: "))
dic['média'] = int(input("Média: "))

print("-="*30)

if dic['média'] >= 7:
    dic['situação'] = 'Aprovado'
elif dic['média'] > 5 and dic['média'] < 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'



for c,v in dic.items():
    if c == 'nome':
        print(f"O aluno: {v}")
    if c =='média':
        print(f"Obteve a média de: {v}")
    if c =='situação':
        if dic['situação'] == 'Aprovado' or dic['situação'] == 'Reprovado':
            print(f"Com estas notas ele está {v}")
        else:
            print(f"Com estas notas ele está de {v}")
print("-="*30)

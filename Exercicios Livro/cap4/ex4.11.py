salario = int(input("Qual o seu salario: "))
valor_casa = float(input("Valor da casa: "))
anos = int(input("Em quantos anos pretende pagar: "))

meses = anos * 12

prestação = valor_casa / meses

if prestação > (salario * 0.30):
    print("Infelizmente não podemos emprestar o dinheiro !")
else:
    print(f"Empréstimo aprovado|Valor da prestação R${prestação:7.2f}")
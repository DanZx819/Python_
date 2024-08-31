print("Bem vindo ao banco para fazer um emprestimo responda as perguntas:")

while True:
    try:
        salario = float(input("Digite o seu salario: "))
        valor = float(input("Digite o valor do empréstimo: "))
        tempo = float(input("Em quantos anos você imagina pagar este empréstimo: "))
        if salario and valor and tempo > 0:
            break
    except ValueError:
        print("Digite um numero!")

porcentagem = (salario * 30) / 100
pagamento_mês = valor / (tempo*12)
arredondado = round(pagamento_mês, 2)
if pagamento_mês > porcentagem:
    print("Você não está aprovado para o empréstimo")
else:
    print("Você esta aceito para o emprestimo!!!")

print(f"""30% do seu salario é {porcentagem} e você vai pagar {arredondado}""")



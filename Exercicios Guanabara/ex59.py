
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
while True:
    menu = int(input("""[1]-Somar
[2]-Multiplicar
[3]-Maior
[4]-Novos numeros
[5]-Sair
Resposta: """))
    soma = valor1 + valor2
    mult = valor1 * valor2
    if menu == 5:
        break
    if menu == 1:
        print(f"A soma dos resultados é {soma}!!!")
    if menu == 2:
        print(f"A Multiplicação é igual a {mult}")
    if menu == 3:
        if valor1 > valor2:
            print(f"O maior numero digitado foi {valor1}")
        else:
            print(f"O maior numero digitado foi {valor2}")
    if menu == 4:
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input("Digite outro valor: "))



while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        if nota1 and nota2 > 0:
            break
    except ValueError:
        print("Digite um numero !!!")



media = (nota1 + nota2) / 2

if media < 5:
    print(f"Sua média {media} é menor que cinco. Reprovado")
elif media > 5 and media < 6.9:
    print(f"Sua média {media} é entre 5 e 6.9. Recuperação")
else:
    print(f"Sua media {media} é maior que 6.9. Aprovado")
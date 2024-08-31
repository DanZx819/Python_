

while True:
    try:
        v = int(input("Qual a velocidade do carro: "))
        if v > 0:
            break
        else:
            print("Digite um numero maior que 0 !")
    except ValueError:
        print("Valor errado")

if v > 80:
    multa = (v - 80)*7
    print(f"""Você está acima da velocidade permitida(80Km/h)!
A sua multa sera de {multa} Reais.""")
else:
    print(f"Parabens a sua velocidade está correta menos de 80Km/h")

    
velocidade = int(input("Qual a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R${multa}")
else:
    print("Você esta dentro dos limites da via!")
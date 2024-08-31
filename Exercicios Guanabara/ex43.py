# peso/(altura x altura). imc

while True:
    try:   
        peso = float(input("Digite o seu peso: "))
        altura = float(input("Digite a sua altura: "))
        if peso and altura > 0:
            break
    except ValueError:
        print("Digite um numero !!!")

Imc = peso / (altura * altura)

print(f"Seu Imc é de {round(Imc,2)}")

if Imc < 18.5:
    print("Seu Imc esta abaixo de 18.5 (Abaixo do Peso)!!!")
elif 18.5 < Imc < 25:
     print("Seu Imc esta entre 18.5 e 25 (Peso ideal)!!!")
elif 25 < Imc < 30:
    print("Seu Imc está entre 25 e 30 (Sobrepeso)!!!")
elif 30 < Imc < 40:
    print("Seu Imc está entre 30 e 40 (Obesidade)!!!")
else:
    print("Seu Imc está maior que 40 (Obesidade Mórbida)!!!")
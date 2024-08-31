import random
cont = 0

while True:
    print("Vamos Jogar impar ou par !!!")
    computador = random.randint(0,10)
    num = int(input("Digite um numero: "))
    soma = num + computador
    escolha = str(input("Você quer Impar ou Par [I/P]: ")).strip().upper()
    if escolha in 'Pp':
        if soma % 2 == 0:
            print(f"Parabens você ganhou você escolheu o número {num} e o computador escolheu {computador} a soma deles é {soma} Par.")
            cont += 1
        else:
            print(f"Você perdeu após ganhar {cont} vezes seguidas.(Você escolheu par e o numero {num} e o computador escolheu {computador} a soma deles é {soma} IMPAR)")
            break
    if escolha in 'Ii':
        if soma % 2 != 0:
            print(f"Parabens você ganhou você escolheu o número {num} e o computador escolheu {computador} a soma deles é {soma} Impar.")
            cont += 1
        else:
            print(f"Você perdeu após ganhar {cont} vezes seguidas.(Você escolheu impar e o numero {num} e o computador escolheu {computador} a soma deles é {soma} PAR)")  
            break  

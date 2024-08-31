import random

Computador = random.randint(1,5)

while True:
    try:
        jogador = int(input("Escolha um numero entre 1 e 5: "))
        if 0 < jogador <= 5:
            break
        else:
            print("Tente Novamente")
    except ValueError:
        print("")



if jogador == Computador:
    print("Parabens você ganhou!!")
else:
    print("Que pena você perdeu")
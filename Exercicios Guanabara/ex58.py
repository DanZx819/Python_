import random

computador = random.randint(0, 10)
print("Computador escolheu um numero!!!")
contadorp = 0
while True:
    ad = int(input("Digite o numero do computador: "))
    if ad == computador:
        print("Você acertou :O")
        break
    else:
        print("Você errou ;-;")
        contadorp += 1

print(f"Você deu {contadorp} palpites")
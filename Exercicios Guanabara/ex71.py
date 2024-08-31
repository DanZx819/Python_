import os
import time
print("="*40)
print(" "*12,"BANCO DO SEXO")
print("="*40)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0


while True:
    try:
        din = int(input("Quanto dinheiro você quer sacar -> R$:"))
        if din > 0:
            break
        else:
            print("Digite um número maior que 0!!!")
    except ValueError:
        print("Digite um número!!!")

while True:
        
        if din - 50 >= 0:
            din -= 50
            nota50 += 1
        elif din - 20 >= 0:
            din -= 20
            nota20 += 1
        elif din - 10 >= 0:
            din -= 10
            nota10 += 1
        elif din - 1 >= 0:
            din -= 1
            nota1 += 1
        else:
            break

print("="*40)
print(f"Você pegou {nota50} notas de R$50.") 
print(f"Você pegou {nota20} notas de R$20.") 
print(f"Você pegou {nota10} notas de R$10.") 
print(f"Você pegou {nota1} notas de R$1.") 
print("="*40)

apagar = str(input("Você quer apagar o terminal [S]"))

for c in range(5, -1, -1):
            print(f"Apagando em {c}...")
            time.sleep(1)
os.system("cls")


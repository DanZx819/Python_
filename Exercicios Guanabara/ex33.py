

while True:
    try:
        num1 = int(input("Primeiro Numero: "))
        break
    except ValueError:
        print("Entrada invalida")      


while True:
    try:
        num2 = int(input("Segundo numero: "))
        break
    except ValueError:
        print("Entrada invalida")      


while True:
    try:
        num3 = int(input("Terceiro numero: "))
        break
    except ValueError:
        print("Entrada invalida")      

numero1 = num1
numero2 = num2
numero3 = num3

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero2 and numero3 > numero1:
    maior = numero3


print(f"O maior numero digitado foi {maior} e o menor foi {menor}")
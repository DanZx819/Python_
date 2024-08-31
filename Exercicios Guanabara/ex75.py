num = (int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")))

cont = num.count(9)
posição = num.index(3)
print("="*30)
print("Números pares -> ",end="")
for n in num:
    if n % 2 == 0:
        print(f"{n}", end=" -> ")
print("FIM")
print(f"Você digitou {cont} vezes o 9")
print(f"A primeira ocorrência do número 3 foi na posição [{posição+1}]")

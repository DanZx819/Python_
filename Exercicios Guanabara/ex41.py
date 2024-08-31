
while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if idade > 0:
            break
    except ValueError:
        print("Digite um numero!!!")

if idade <= 9:
    print("Categoria Mirim")
elif 9 < idade < 14:
    print("Categoria Infantil")
elif 14 < idade < 19:
    print("Categoria Junior")
elif 19 < idade < 21:
    print("Categoria Sênior")
else:
    print("Categoria Master")
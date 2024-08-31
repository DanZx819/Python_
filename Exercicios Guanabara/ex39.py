



while True:
    try:
        idade = int(input("Quantos anos você tem ?: "))
        if idade > 0:
            break
    except ValueError:
        print("Digite um numero !!!")

if idade == 18:
    print("Está na hora de se alistar")
elif idade < 18:
    print(f"Ainda não é a hora de se alistar falta {18 - idade} anos para se alistar.")
else:
    print(f"Você ja deveria ter se alistado, passou {idade - 18} anos.")







while True:
    try:
        dis = float(input("Qual a distância da sua viagem ?: "))
        if dis > 0:
            break
        else:
            print("Digite um valor acima de 0!")
    except ValueError:
        print("Valor invalido tente novamente")

if dis <= 200:
    preço = 0.50 * dis
else:
    preço = 0.45 * dis

print(f"""A sua viagem vai ficar em {preço} """)


while True:
    try:
        ano = int(input("Em que ano estamos: "))
        if ano > 0:
            break
        else:
            print("Digite um ano valido")
    except ValueError:
        print("Entrada invalida")

if ano % 4 == 0:
    print(f"{ano} é Bissexto.")
else:
    print(f"{ano} Não é bissexto.")
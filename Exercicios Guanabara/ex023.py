while True:
    
    try:
        numero = int(input("Digite um numero de 0 a 9999: "))
        if 0 <= numero <= 9999:
            break
        else:
            print("Tente Novamente numero inválido")
    except ValueError:
        print("Digite um numero valido entre 0 e 9999")


numero = str(numero)
dividir = list(numero)

if len(dividir) == 4:
    print(f"""Unidade: {dividir[0]}
Dezena: {dividir[1]}
Centena: {dividir[2]}
Milhar: {dividir[3]}""")
elif len(dividir) == 3:
    print(f"""Unidade: {dividir[0]}
Dezena: {dividir[1]}
Centena: {dividir[2]}""")
elif len(dividir) == 2:
    print(f"""Unidade: {dividir[0]}
Dezena: {dividir[1]}""")
elif len(dividir) == 1:
    print(f"Unidade: {dividir[0]}")
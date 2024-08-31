sexo = ''

while sexo not in ['M', 'F']:
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper()
    if sexo in ['M', 'F']:
        print(f"Sexo registrado {sexo}.")
    else:
        print("Digite um sexo valido!!!")
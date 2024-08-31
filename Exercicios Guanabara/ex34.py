

while True:
    try:
        sal = float(input("Qual o seu salario: "))
        break
    except ValueError:
        print("Entrada invalida")
     

if sal > 1250:
    aum = (sal * 10) / 100
    sal2 = aum + sal
    print(f"O seu aumento foi de {aum} e agora o total é {sal2}")
else:
    aum = (sal * 15) / 100
    sal2 = aum + sal
    print(f"O seu aumento foi de {aum} e agora o total é {sal2}")

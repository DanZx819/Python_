def reta1():
    while True:
        try:
            reta1 = int(input("Digite os valores das retas: "))
            if reta1 > 0:
                break
            else:
                print("Digite um numero maior que 0")
        except ValueError:
            print("Entrada invalida")
    return reta1


reta = reta1()
reta2 = reta1()
reta3 = reta1()

if reta + reta2 < reta3:
    print("Da pra fazer o triangulo !!!")
else:
    print("Não da pra fazer o Triângulo.")
if reta + reta3 < reta2:
    print("Da pra fazer o triangulo !!!")
else:
    print("Não da pra fazer o Triângulo.")
if reta2 + reta3 < reta:
    print("Da pra fazer o triangulo !!!")
else:
    print("Não da pra fazer o Triângulo.")


if reta == reta2 == reta3:
    print("Você vai ter um triangulo Equilatero!!!")
elif reta == reta2 or reta2 == reta3 or reta == reta3:
    print("Você vai ter um triangulo Isóceles!!!")
else:
    print("Você vai ter um triangulo Escaleno!!!")
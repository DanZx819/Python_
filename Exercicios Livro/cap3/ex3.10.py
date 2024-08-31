salario = float(input("Salario: "))
aumento = float(input("Aumento: "))
aum = (salario * aumento / 100)
salario_aumentado= salario + aum
print(f"Com o salario de {salario} e o aumento de {aumento}% você vai ter um aumento de {aum} e um novo salario de {salario_aumentado}")
salario = float(input("Qual o seu salario: "))

if salario > 1250:
    aumento = salario +(salario * 0.10)
    print(f"Com o salario de {salario} teve um aumento de 10% tornando {aumento}")
else:
    aumento = salario +(salario * 0.15)
    print(f"Com o salario de {salario} teve um aumento de 15% tornando {aumento}")
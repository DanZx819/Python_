num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
conta = str(input("Escolha a operação (+|-|/|*): ")).strip()

if conta in "+":
    resultado = num1 + num2
    print(f"O resultado foi {resultado}")
elif conta in "-":
    resultado = num1 - num2
    print(f"O resultado foi {resultado}")
elif conta in "/":
    resultado = num1 / num2
    print(f"O resultado foi {resultado}")
elif conta in "*":
    resultado = num1 * num2
    print(f"O resultado foi {resultado}")
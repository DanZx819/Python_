def leiaint(int):
    while True:
        s = input(int)
        if str(s).isnumeric() == True:
            return s
            break
        else:
            print("Erro digite um número")






n = leiaint("Digite um numero: ")
print(f"Você digitou o numero {n}")
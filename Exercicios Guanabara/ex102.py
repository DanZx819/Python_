def fatorial(n):
    """
    Vai receber um número
    vai fazer um looping para retirar 1 e multiplicar
    vai retornar o fatorial
    """
    f = 1
    for c in range(n,0,-1):
        f *= c
        print(f"{c}x{c-1}", end=" ")
    print("= ", end='')
    return f

fatorialc = int(input("Digite um número: "))
print(fatorial(fatorialc))
help(fatorial)
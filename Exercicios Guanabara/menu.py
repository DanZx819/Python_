import time
def menu(msg):
    time.sleep(0.5)
    print("-"*35)
    print("           Menu Inicial")
    print("-"*35)
    print("1 - Pessoas Cadastradas")
    print("2 - Cadastrar uma nova pessoa")
    print("3 - Sair")
    print("-"*35)
    while True:
        try:
            opc = int(input(msg))
            return opc
            break
        except:
            print("Erro digite uma opção valida")

lista = []
pessoas = {}
def opc1():
    time.sleep(0.5)
    i = 'OPÇÃO 1'
    print("-"*35)
    print(f"{i:>20}")
    print("-"*35)
    print("Cod", end='')
    for i in pessoas.keys():
        print(f"{str(i).title():>10}", end=' ')
    print()
    for I,v in enumerate(lista):
        print(f"{str(I):<3}", end='')
        for d in v.values():
            print(f"{str(d):>10}", end="")
        print()
            

    print()
    while True:
        esc = str(input("Quer sair [S/N]:")).strip().upper()
        if esc in 'S':
            break
        else:
            print("Ok | ", end='')
            
def opc2():
    time.sleep(0.5)
    i = 'OPÇÃO 2'
    print("-"*35)
    print(f"{i:>20}")
    print("-"*35)
    while True:
            pessoas['nome'] = str(input("Nome: ")).strip()
            if pessoas['nome'] in '':
                print("Erro digite um nome!!!")
            else:
                break
    while True:
        try:
            pessoas['idade'] = int(input("Idade: "))
        except:
            print("Digite um número")
        else:
            lista.append(pessoas.copy())
            break

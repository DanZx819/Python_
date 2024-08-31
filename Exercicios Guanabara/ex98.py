
def contador(ini, fim, quant):
    print("-"*30)
    print("Inicio -> ",end='')
    if ini < fim:
        for i in range(ini, fim+1,quant):
            print(f"{i}", end=' ')
    else:
        for i in range(ini,fim,-quant):
            print(f"{i}", end=' ')
    print("-> FIM")
    print("-"*30)

contador(1,10,1)
contador(10,1,2)

print("Agora é a sua vez de personalizar!!!")
inicio = int(input("Inicio: "))
final = int(input("Final: "))
quanto = int(input("De quanto em quanto: "))

contador(inicio,final,quanto)


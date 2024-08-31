lista = []

maior = 0
menor = 0
for c in range(0,5):
    valores = int(input("Digite um numero: "))
    lista.append(valores)

lista.sort()

print("Lista -> ",end='')
for n in lista:
    print(f"{n} ",end='')


    


    
       
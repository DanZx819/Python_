
valores = []
maior = 0
menor = 0
print("="*30)
print(' '*8,end='')
print("Maior e menor")
print("="*30)
for i in range(0,5):
    #input 5 vezes
    valor = int(input(f"Digite um número para a posição {i}: "))
    valores.append(valor)
    #Checkar se é maior
    if i == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

for a,v in enumerate(valores):
    #Contar a posição pelo a
    #E o valor pelo v
    if v == maior:#Se o valor v for o maior 
        pmaior = a#pmaior = posição (a)
    if v == menor:
        pmenor = a

print(f"Maior:{maior}|Está na posição:{pmaior}")
print(f"Menor:{menor}|Está na posição:{pmenor}")

 
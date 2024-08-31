lista = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    pergunta = str(input("Você quer continuar [S/N]: "))
    if pergunta in 'Nn':
        break
cinco = 0
for c in lista:
    if c == 5:
        cinco +=1
print("="*30)
if cinco > 0:
    print(f"A lista possue 5")
else:
    print(f"A lista não possue 5")
print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(f"Lista na ordem decresente ->[{lista}]")
print("="*30)
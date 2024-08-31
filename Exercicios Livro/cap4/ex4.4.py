distancia = int(input("Qual a distância da viagem: "))

if distancia <= 200:
    preço = distancia * 0.50
    print(f"Preço da viagem R${preço:.2f}")
else:
    preço = distancia * 0.45
    print(f"Preço da viagem R${preço:.2f}")
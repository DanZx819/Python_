print(f"Você alugou um carro !!!")
dias = int(input("Por quantos dias: "))
distancia_km = int(input("Percorreu quantos Km: "))
preço = dias * 60 + distancia_km * 0.15

print(f"Você pagára R${preço} pelo aluguel")
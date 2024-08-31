import moeda

preço = float(input("Valor em R$: "))
print(f"Aumentando 10% temos R${moeda.aumentar(preço)}")
print(f"O dobro é R${moeda.dobro(preço)}")
print(f"E a metade é R${moeda.metade(preço)}")
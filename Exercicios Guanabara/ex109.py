import moeda

preço = float(input("Valor em R$: "))
print(f"Aumentando 10% de {moeda.format(preço)} temos {moeda.aumentar(preço, 10, True)}")
print(f"O dobro de {moeda.format(preço)} é {moeda.dobro(preço, True)}")
print(f"E a metade de {moeda.format(preço)} é {moeda.metade(preço,True)}")
print(f"Diminuindo 13% de {moeda.format(preço)} temos {moeda.diminuir(preço, 13,True)}")
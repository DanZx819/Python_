preço = float(input("Preço: "))
desconto = float(input("Desconto em %: "))

preço_descontado = preço - (preço * desconto / 100)
print(f"Preço total foi de {preço_descontado}")
lista = ('Caneta', 1.75, 'Lapis', 1.00, 'Borracha', 2.00, 'Apontador', 5.00, 'Caderno', 25.00)
print("="*30)
print(" "*12, end='')
print("Lista")
print("="*30)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}",end='')
    else:
        print(f"R${lista[pos]: >1}")

print("="*30)
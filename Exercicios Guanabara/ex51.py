
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
décimo = termo + (11-1) * razao
for c in range(termo, décimo, razao):
    print(c)
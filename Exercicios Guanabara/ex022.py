
nome = input("Digite o seu nome completo:")

M = nome.upper()
m = nome.lower() 
c = nome.split()
n1 = len(c[0])
j = ''.join(c)
Leitura = len(j)
print(f"""Nome completo: {nome}
Maiuscula: {M}
Minuscula: {m}
Quantidade de letras: {Leitura}
Quantidade de letras no primeiro nome: {n1}""")

print(f"{j}")
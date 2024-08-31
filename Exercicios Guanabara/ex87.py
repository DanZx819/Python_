
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor({l},{c}): "))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if matriz[l][c] == 0:
            maior = matriz[l][c]
        else:
            if matriz[0][c] > maior:
                maior = matriz[0][c]
            

            

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f"""[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]
[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]
[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]""")
print(f"Soma dos números da terceira coluna -> {soma}")
print(f"Números pares digitados -> {pares}")
print(f"Maior número da linha 0 -> {maior}")

  
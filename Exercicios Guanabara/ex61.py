termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
primeiro = termo
contador = 1
mais = 0

while contador == 0:

    while contador <= 10:
        primeiro =  primeiro + razao
        print(f"{primeiro} →", end=" ")
        contador += 1
print("Fim")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
primeiro = termo
contador = 1
mais = 10
total = 10
cont = 0
while mais != 0:

    while contador <= total:
        primeiro =  primeiro + razao
        print(f"{primeiro} → ", end="")
        contador += 1
    print(" Pausa...")
    mais = int(input("Você quer ver quantos termos a mais: "))
    total += mais
    cont = total + mais
print(f"Você pegou {cont} numeros de uma PA")
print("Fim")
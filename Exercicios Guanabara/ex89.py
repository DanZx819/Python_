import os
import time
lista = []
temp = []
while True:
    Nome = str(input("Nome: "))
    temp.append(Nome)
    Nota1 = int(input("Nota 1: "))
    temp.append(Nota1)
    Nota2 = int(input("Nota 2: "))
    temp.append(Nota2)

    lista.append(temp[:])
    temp.clear()

    pergunta = str(input("Você quer continuar [S/N]:"))
    if pergunta in "Nn":
        break
print("""No     Nome   Média""")


for n,d in enumerate(lista):
    media = (lista[n][1] + lista[n][2]) / 2
    print(f"{n}     {d[0]}  {media}")
    

while True:
    continuar = str(input("Você quer continuar [999] para sair: "))

    if continuar in '999':
        print("Fechando...", end="")
        time.sleep(3)
        break
    else:
        nm = int(input("Digite um número: "))
        if nm <= len(lista):
            print(f"O aluno {lista[nm][0]} tirou: {lista[nm][1]} e {lista[nm][2]}") 

os.system("cls")







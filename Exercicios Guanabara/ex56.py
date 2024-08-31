




def analisador():
    somaidade = 0
    mediaidade = 0
    maioridadehomem = 0
    mulhermenos20 = 0
    nomemvelho = '' 
    while True:
        try:
            começo = input("Vamos começar S/N?")
            if começo != 's':
                break

            for l in range(1 ,6):
                print(f"========== PESSOA {l} ==========")
                nome = str(input("Digite o seu nome: ")).strip()
                idade = int(input("Digite a sua idade: "))
                sexo = str(input("Digite o seu sexo [M/F]: ")).strip()
                somaidade += idade
                if 'Mm' in sexo:
                    sexo += sexo.upper()
                if sexo in 'Ff' and idade <20:
                    mulhermenos20 += 1
                if l == 1 and sexo in 'Mm':
                    maioridadehomem = idade
                    nomemvelho = nome
                if sexo in 'Mm' and idade > maioridadehomem:
                    maioridadehomem = idade
                    nomemvelho = nome 
        except ValueError:
            print("Tente novamente!!!")

        mediaidade = somaidade / l

        print(f"A média das idades é {mediaidade}.")
        print(f"O homem mais velho é o {nomemvelho} com {maioridadehomem} anos.")
        print(f"{mulhermenos20} mulheres tem menos de 20 anos.")

while True:
    analisador()
    try:
        continuar = str(input("Você quer continuar ? S/N"))
        if continuar != 's':
            print("Saindo...")
            break
    except ValueError:
        print("Escreve direito!!!")

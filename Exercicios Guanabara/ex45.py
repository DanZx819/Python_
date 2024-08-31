import random


def escolha():
    while True:
        try:
            escolha = int(input("Vamos jogar pedra papel tesoura\nEscolha entre os 3\n1- Pedra \n2- Papel\n3- Tesoura\n0- Para Sair\n"))
            if escolha == 0:
                break
            if escolha == 1:
                escolhae = str("Pedra")
            elif escolha == 2:
                escolhae = str("Papel")
            elif escolha == 3:
                escolhae = str("Tesoura")
            
            #Randomizar a escolha do Computador
            computador = random.randint(1,3)
            #Escolha do computador
            if computador == 1:
                computadore = str("Pedra")
            elif computador == 2:
                computadore = str("Tesoura")
            else:
                computadore = str("Papel")
            
            
            #Quem Ganhou caso 1
            if computador == 1 and escolha == 2:
                print(f"Você ganhou!!! Computador:{computadore} x Você:{escolhae}")
            elif computador == 1 and escolha == 1:
                print(f"Empate!!! Computador:{computadore} x Você:{escolhae}")
            elif computador == 1 and escolha == 3:
                print(f"Você perdeu!!! Computador:{computadore} x Você:{escolhae}")
            
            
            #Quem Ganhou caso 2
            if computador == 2 and escolha == 2:
                print(f"Você Perdeu!!! Computador:{computadore } x Você:{escolhae}")
            elif computador == 2 and escolha == 1:
                print(f"Você Ganhou!!! Computador:{computadore} x Você:{escolhae}")
            elif computador == 2 and escolha == 3:
                print(f"Empate!!! Computador:{computadore} x Você:{escolhae}")
            
            #Quem ganhou caso 3       
            if computador == 3 and escolha == 2:
                print(f"Empate!!! Computador: {computadore} x Você:{escolhae}")
            elif computador == 3 and escolha == 1:
                print(f"Você Perdeu!!! Computador:{computadore} x Você:{escolhae}")
            elif computador == 3 and escolha == 3:
                print(f"Você Ganhou!!! Computador:{computadore} x Você:{escolhae}")
            
        except ValueError:
            print("Digite uma entrada valida!!!")

while True:
    escolha()
    continuar = str(input("Você deseja continuar ? S/N\n"))
    if continuar.lower != "s":
        print("Saindo...")
        break


def menu():
    while True:
        try:
            pagamento = int(input("""Qual a forma de pagamento 
1- dinheiro/cheque
2- A vista no cartão
3- 2x no cartão
4- 3x ou mais no cartão
0 - Para Sair\n"""))
            if pagamento == 0:
                break
            if pagamento in [1,2,3,4]:
                preço = float(input("Qual o preço ?\n"))
            
                match pagamento:
                    case 1:
                        desconto = preço-((preço * 10) / 100)
                        print(f"Você pagara {desconto} ao invés de {preço} pois vai pagar no dinheiro.")
                    case 2:
                        desconto = preço-(preço * 5) / 100
                        print(f"Você pagara {desconto} ao invés de {preço} pois vai pagar a vista no cartão.")
                    case 3:
                        desconto = pagamento
                        print(f"Você pagara o mesmo tanto {desconto}")    
                    case 4:
                        juros = ((preço * 20) / 100) + preço
                        print(f"Você pagara {juros - preço} a mais por conta dos juros totalizando {juros}")
        except ValueError:
            print("Digite uma das opções 1/2/3/4")


while True:
    menu()
    continuar = str(input("Você deseja continuar S/N\n"))
    if continuar.lower() != "s":
        print("Saindo...")
        break
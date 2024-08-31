
def calculadora():

    while True:    
    
            menu = input("Digite + - / x ou 0 para sair\n")

            
            if menu == "0":
                 break
            
            if menu in ["+", "-", "x", "/"]:
                try:
                    numero1 = int(input("Digite o primeiro numero: "))
                    numero2 = int(input("Digite o segundo numero: "))

                    match menu:
                            case "+": 
                                resultado = numero1 + numero2
                            case "-":
                                resultado = numero1 - numero2
                            case "x":
                                resultado = numero1 * numero2
                            case "/":
                                if numero2 == 0:
                                    print("Não da pra dividir por 0")
                                    continue
                                resultado = numero1 / numero2
                    print(f"Resultado: {resultado}")        
                except ValueError:
                    print("Entrada invalida tente novamente")
            else:
                print("Operação invalida Tente Novamente")             

while True:
    calculadora()
    continuar = input("Você deseja continuar S/N?\n").strip().lower()
    if continuar != "s":
        print("Saindo...")
        break
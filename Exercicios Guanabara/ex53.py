

def frase():
    while True:
        try:
            frase = str(input("Digite uma frase (Ou 0 para sair): ")).strip().upper()
            if frase == "0":
                break
            palavras = frase.split()
            juntar = "".join(palavras)
            inverter = ""
            for letra in range(len(juntar)-1, -1, -1):
                inverter += juntar[letra]
            print(inverter, juntar)
            if juntar == inverter:
                print("É um palindromo")
            else:
                print("Não é um palindromo")


        except ValueError:
            print("Tente Novamente!!!")


while True:
    frase()
    continuar = str(input("Você deseja sair mesmo S/N: ")).lower()
    if continuar == "s":
        break







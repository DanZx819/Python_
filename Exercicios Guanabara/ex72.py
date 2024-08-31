extenso = ("Zero", "Um","Dois","Três","Quatro","Cinco","Seis","Sete"
            "Oito","Nove","Dez","Onze","Doze","Treze","Quatorze","Quinze"
            "Dezeseis","Dezesete","Dezoito","Dezenove","Vinte")

while True:
    try:
        pergunta = int(input("Digite um numero entre 0 e 20:"))
        if pergunta > 0 and pergunta < 20:
            break
        else:
            print("Digite um número entre 0 e 20!!!")
    except ValueError:
        print("Digite um número!!!")

print(f"Você digitou o número {pergunta}")
print(f"Extenso:{extenso[pergunta]}")
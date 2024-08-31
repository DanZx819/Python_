
contador = 0 
contador2 = 0

for pess in range (1,8):
    pergunta = int(input(f"Digite o ano em que a {pess} pessoa nasceu: "))
    if pergunta > 2006:
        print("Não é maior")
        contador = contador +1
    else:
        print("É maior")
        contador2 = contador2 +1
    

print(f"Destas idades que voce digitou {contador} pessoas ainda não atingiram a maioridade.\nE as pessoas que chegaram na maioriadade são {contador2}.")
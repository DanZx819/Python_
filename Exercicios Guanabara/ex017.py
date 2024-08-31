import math
#Comentário loop while vem como verdadeiro ele tenta pegar um input do tipo float se for do tipo float o loop encerra exceto quando o usuario digita um caractere ai ele da um erro e repete o loop
while True:
    try:
        an = float(input("Digite um angulo: "))
        break
    except ValueError:
        print("Entrada invalida tente escrever um numero.")
        
    
se = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))

print(f"O seno de {an} é {round(se, 2)}\nO coseno de {an} é {round(cos, 2)}\nA tangente de {an} é {round(tang, 2)}")
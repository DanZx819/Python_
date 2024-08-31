from datetime import datetime

def voto(num):
    idade = datetime.now().year - num
    if idade >= 18 and idade < 70:
        print(f"Com {idade} anos -> Voto Obrigatório")
    if idade < 18 and idade > 15:
        print(f"Com {idade} anos -> Voto opcional")    
    if idade > 70:
        print(f"Com {idade} anos -> Voto opcional")   
    if idade < 15:
        print(f"Com {idade} anos -> Não vota")
    
    return idade

ano = int(input("Em que ano você nasceu ?: "))
voto(ano)
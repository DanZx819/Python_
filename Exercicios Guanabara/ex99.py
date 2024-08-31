import time
def maior(* num):
    maior = 0
    cont = 0
    print("-="*15)
    print("Analisando os valores ",end='')
    for valor in num:
        print(f" {valor}", end='', flush=True)
        time.sleep(0.1)
        if cont == 0:
            maior = valor
        if valor > maior:
            maior = valor
        cont += 1
    print()
    print(f"Foram informados {cont} valores")
    print(f"Maior número = {maior}")
    

maior(0,1,2,3,4,5,6,7,8,9,10)
maior(9,2,1,13,24,2,0)

import time
import requests


link = "https://economia.awesomeapi.com.br/last/BRL-USD,USD-BRL,EUR-BRL,BTC-BRL"

req = requests.get(link)

dados = req.json()

cotacao_dolar = dados["USDBRL"]["bid"]

cotdol = float(cotacao_dolar)

cotacao_euro = dados["EURBRL"]['bid']

coteu = float(cotacao_euro)

def menu(str):
    time.sleep(0.5)
    print("-"*30)
    print(f"     Conversor de Moedas")
    print("-"*30)
    print("1-Digite um valor em R$")
    print("2-Converta para U$")
    print("3-Converta para €")
    print("4-Sair")
    print("-"*30)
    
    while True:
        time.sleep(0.5)
        try:
            e = int(input(str))
            if e == 1 or e == 2 or e == 3 or e == 4:
                
                break
            else:
                print("Digite uma opção valida!!!")
        except:
            print("Digite um Número!!!")
    return e


def format(num = 0, moeda ='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')



def valoreal():
    time.sleep(0.5)
    while True:
        try:
            r = float(input("Digite o valor: "))
            print(f"Valor digitado foi {format(r)}")
            break
            
        except:
            print("Digite um número")
    while True:
        pergunta = str(input("Você quer continuar [S/N]: ")).upper()
        if pergunta in "S":
            break
        else:
            print("Ok |", end="")
    return r

def dollar(a=0):
    time.sleep(0.5)
    dol = a / cotdol
    print(f"Valor convertido de Real para Dollar -> {format(dol, moeda= 'U$')}")
    while True:
        pergunta = str(input("Você quer continuar [S/N]: ")).upper()
        if pergunta in "S":
            break
        else:
            print("Ok |", end="")

def euro(a=0):
    time.sleep(0.5)
    eu = a / coteu
    print(f"Valor convertido de Real para EURO -> {format(eu, moeda='€')}")
    while True:
        pergunta = str(input("Você quer continuar [S/N]: ")).upper()
        if pergunta in "S":
            break
        else:
            print("Ok |", end="")
    
    
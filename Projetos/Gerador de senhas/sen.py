import string
import random


def inicial():
    print('-' *30)
    print("      Gerador de senhas")
    print('-' * 30)



   

def senha():
    
    while True:
        try:
            tamanho = int(input("Qual é o tamanho da sua senha: "))
            if tamanho > 0:
                break
        except ValueError:
            print("Digite um número !!!")

    while True:
        per = str(input("A sua senha vai ter letras maiusculas [S/N]:")).upper()
        if per == 'S' or per == 'N':
            letraM = per
            break
        else:
            print("Digite S ou N!!!")
    
    while True:
        perm = str(input("A sua senha vai ter letras minusculas [S/N]:")).upper()
        if perm == 'S' or perm == 'N':
            letram = perm
            break
        else:
            print("Digite S ou N!!!")


    while True:
        pern = str(input("A sua senha vai ter numeros [S/N]:")).upper()
        if pern == 'S' or pern == 'N':
            numeros = pern
            break
        else:
            print("Digite S ou N!!!")
    while True:
        perc = str(input("A sua senha vai ter caracteres especiais [S/N]:")).upper()
        if pern == 'S' or pern == 'N':
            caracteres_especiais = perc
            break
        else:
            print("Digite S ou N!!!")


    letra_M = string.ascii_uppercase
    letra_m = string.ascii_lowercase
    num = string.digits
    arroba = string.punctuation
    caracteres = ''

    if letraM == 'S':
        caracteres += letra_M
    if letram == 'S':
        caracteres += letra_m
    if numeros == 'S':
        caracteres += num
    if caracteres_especiais == 'S':
        caracteres += arroba
    
    senha_final = ''

    for c in range(tamanho):
        senha_final += random.choice(caracteres)
    return senha_final

def final():
    print('-' *30)
    print("    Senha segura gerada")
    print('-' * 30)
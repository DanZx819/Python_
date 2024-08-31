def leianum(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",",".").strip()
        if entrada.isalpha() or entrada in ' ' :
            print(f"Erro \"{entrada}\" digite um número valido!!!")
        else:
            valido = True
            return float(entrada)


def resumo(num=0, au=0, dm=0):
    print("-"*20)
    print(f"Preço Analisado: {format(num)}")
    print(f"Dobro: {dobro(num, True)}")
    print(f"Metade: {metade(num, True)}")
    print(f"Aumento de {au}%: {aumentar(num,au, True)}")
    print(f"Diminuição de {dm}%: {diminuir(num,dm, True)}")
    print("-"*20)

def format(num = 0, moeda ='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')

def diminuir(num = 0, x=0, form = False):
    dm = num -(num / 100)*x
    return dm if form is False else format(dm)


def aumentar(num = 0,x=0,form = False):
    au =num + (num / 100)*x
    return au if form is False else format(au)


def metade(num = 0, form = False):
    met = num / 2
    return met if form is False else format(met)


def dobro(num = 0, form = False):
    dob = num * 2
    return dob if form is False else format(dob)
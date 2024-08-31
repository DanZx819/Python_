def leiaint(msg):
    while True:
        try:
            s = int(input(msg))
            return s
            break
        except:
            print("Erro digite um número")

def leiafloat(msg):
    while True:
        try:
            s = float(input(msg))
            return s
            break
        except:
            print("Erro digite um número")

a = leiaint("Digite um número: ")
b = leiafloat("Digite um número com virgula: ")
print(a, b)




while True:
    Nota = float(input("Digite a primeira nota: "))
    if 0 <= Nota <= 10:
        break
    else:
        print("Erro(Nota 1): Digite uma nota entre 0 e 10")

while True:
    Nota2 = float(input("Digite a segunda nota: "))
    if 0 <= Nota2 <= 10:
        break
    else:
        print("Erro(Nota 2): Digite uma nota entre 0 e 10")

m = (Nota + Nota2) / 2

print(f"A média deste aluno é {m}")
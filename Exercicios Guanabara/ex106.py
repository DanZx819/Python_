def ajuda(str):
    print(help(str))


while True:
    per = str(input("Digite uma biblioteca ou função> "))
    if per == "FIM":
        break
    else:
        ajuda(per)




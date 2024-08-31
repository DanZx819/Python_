import sen

while True:
    sen.inicial()

    senha_segura = sen.senha()

    sen.final()

    print(f"{senha_segura}")
    
    continuar = str(input("VocÊ quer gerar outra senha [S/N]: ")).strip().upper()
    if continuar in "N":
        print(f"Vai la utilize a sua senha ('{senha_segura}'')")
        break
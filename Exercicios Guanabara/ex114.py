import menu

while True:
    escolha = menu.menu("Escolha: ")
    if escolha == 1:
        menu.opc1()
    elif escolha == 2:
        menu.opc2()
    elif escolha == 3:
        break

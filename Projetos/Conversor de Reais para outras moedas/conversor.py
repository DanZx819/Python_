import conv

menu = conv.menu("Digite uma opção: ")
while True:
    if menu == 1:
        Valor = conv.valoreal()
        menu = conv.menu("Digite uma opção: ")
    if menu == 2:
        convdollar = conv.dollar(Valor)
        menu = conv.menu("Digite uma opção: ")
    if menu == 3:
        conveuro = conv.euro(Valor)
        menu = conv.menu("Digite uma opção: ")
    if menu == 4:
        break
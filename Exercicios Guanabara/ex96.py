def area(comprimento, largura):
    calc = comprimento * largura
    print(f"A area de um terreno {comprimento}mx{largura}m = {calc}m2")



comprimento = int(input("Comprimento em M: "))
largura = int(input("Largura em M: "))

area(comprimento, largura)
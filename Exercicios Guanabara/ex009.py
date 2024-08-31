d = 5
g = int(input("Você ganha em dollares ou em reais ?\n1-Para reais\n2-Para dollares\n"))
di = 0

while g > 2 or g <= 0:
   g = 0
   g = int(input("Você ganha em dollares ou em reais ?\n1-Para reais\n2-Para dollares\n"))

if g == 1:
   c = float(input("Quanto reais você tem na carteira: "))
   cc = c / d
else:
   cd = float(input("Quanto dollares você tem na carteira: "))

if g == 2:
    cdd = cd * d
    print(f"Você podera comprar {cdd} reais com {cd} dollares ")
else:
    print(f"Você podera comprar {cc} dolares com {c} reais")
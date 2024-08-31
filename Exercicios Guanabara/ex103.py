

def ficha(jog='<desconhecido>',gols=0):
    print(f"O jogador {jog} fez {gols} gol(s).")

n = str(input("Digite o seu nome: "))
g = str(input("Quantos gols ele fez:"))

if g.isnumeric:
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)


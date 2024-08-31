
pd = int(input("Por quantos dias você alugou ?\n"))
pk = float(input("Quantos Km você rodou ?\n"))

d = 60 * pd
km = 0.15 * pk
t  = d + km

print(f"Você pagara {t}R$ no aluguel deste carro\nDias alugados:{pd}\nKm rodados: {pk}Km")
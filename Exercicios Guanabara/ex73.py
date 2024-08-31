times = ("Botafogo","Palmeiras","Flamengo","Bahia","Cruzeiro","São Paulo","Fortaleza"
        "Atletico-PR","Bragantino","Atletico-MG","Vasco da Gama","Internacional",
        "Juventude","Criuma","Cuiaba","EC-Vítoria","Corinthians","Grêmio","Atlico-GO",
        "Fluminense")

print(f"Primeiros 4 colocados -> {times[0:4]}")
print(f"Ultimos times -> {times[-4:]}")
print(f"Ordem alfabética{sorted(times)}")
print(f"O Corinthians está na {times.index("Corinthians")+2} posição.")

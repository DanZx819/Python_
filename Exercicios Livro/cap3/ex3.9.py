dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

segd = (dias * 24 *60 *60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"Você tem {segd} em relação aos dados digitados")


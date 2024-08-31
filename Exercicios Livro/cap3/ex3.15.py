qnt_cigarro_dia = int(input("Quantos cigarros você fuma por dia: "))
qnt_anos_fuma = int(input("Quantos anos você fuma: "))

quantidade_cigarro_pordia = (qnt_anos_fuma * 365) * qnt_cigarro_dia
transformar_em_dias = quantidade_cigarro_pordia / 60 / 24
print(f"Nesse ritmo você vai perder {transformar_em_dias:.2f} dias da sua vida")

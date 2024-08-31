# Calculo da Mensalidade da Operadora

plano = str(input("Plano 1 ou plano 2: "))

if plano == '1':
    minutos_plano = 100
    extra = 0.20
    preço = 50

if plano == '2':
    minutos_plano = 500
    extra = 0.15
    preço = 99

if plano != '1' and plano != '2':
    print("Não conheço este plano ")

if plano == '1' or plano == '2':
    minutos_consumidos = int(input("Quantos minutos foram consumidos: "))

    if plano == '1' and minutos_consumidos > 100:
        mais = extra*(minutos_consumidos - minutos_plano)
        print(f"Preço do plano {preço} extra {mais} total {preço + mais}")
    else:
        if plano == '1':
            print(f"Preço do plano {preço} total {preço}")
    
    if plano == '2' and minutos_consumidos > 500:
        mais = extra*(minutos_consumidos - minutos_plano)
        print(f"Preço do plano {preço} extra {mais} total {preço + mais}")
    else:
        if plano == '2':
            print(f"Preço do plano {preço} total {preço}")
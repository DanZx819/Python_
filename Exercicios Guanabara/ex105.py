def notas(*n ,sit=False):
    ficha = {}
    ficha['notas'] = n
    
    tot = 0
    maior = 0
    menor = 0
    cont = 0
    for c in ficha['notas']:
        tot += c
    ficha['total'] = tot
    for a in ficha['notas']:
        if cont == 0:
            maior = a
            menor = a
            cont += 1
        else:
            if a > maior:
                maior = a
            if a < menor:
                menor = a
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['media'] = tot / len(ficha['notas'])
    if sit:
        if ficha['media'] > 8.5:
            ficha['situação'] = 'Ótima'
        if ficha['media'] > 7 and ficha['media'] < 8.5:
            ficha['situação'] = 'Boa'
        if ficha['media'] < 7 and ficha['media'] > 5:
            ficha['situação'] = 'Razoavel'
        if ficha ['media'] < 5:
            ficha['situação'] = 'Ruim'
    return ficha







resp = notas(7,10,9,9, sit=True)
print(f"{resp}")
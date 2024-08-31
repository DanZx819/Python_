

palavras = ('Alberto','Carlos','Daniel')
print("-"*30)
print(" "*6, end='')
print("Detector de vogais")
print("-"*30,end='')
for p in palavras:
    print(f"\nPalavra -> {p} Vogais -> ", end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f"{l}", end=' ' )

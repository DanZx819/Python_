maior = 0
menor = 0
for peso in range(1, 7):
    pergunta = int(input(f"Qual o peso da {peso} pessoa: "))
    
    if peso == 1:
        maior = pergunta
        menor = pergunta
    else:
        if pergunta > maior:
            maior = pergunta
        if pergunta < menor:
            menor = pergunta

print(f"O maior peso registrado foi {maior}Kg e o menor foi {menor}Kg.")


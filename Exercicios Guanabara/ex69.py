contidade = 0
contpessoas = 0
conthomem = 0
contmulher = 0
idade = 0
sexo = ''
continuar = ''
while True:
    idade = int(input("Quantos anos você tem: "))
    sexo = str(input("Qual o seu sexo [M/F]: "))
    contpessoas += 1
    if sexo in "Mm":
        conthomem += 1
    elif sexo in "Ff" and idade < 20:
        contmulher += 1
    if idade > 18:
        contidade += 1
    continuar = str(input("Você quer continuar [S/N]: "))
    if continuar in 'Nn':
        print("="*50)
        if contpessoas > 1:
            print(f"Você cadastrou {contpessoas} pessoas.")
        else:   
            print(f"Você cadastrou {contpessoas} pessoa.")
        if conthomem > 1:
            print(f"{conthomem} homens foram cadastrados.")
        else:
            print(f"{conthomem} homem foi cadastrado.")
        if contmulher > 1:
            print(f"{contmulher} mulhereres com menos de 20 anos foram cadastradas.")
        else:
            print(f"{contmulher} mulher com menos de 20 anos foi cadastrada.")
        if contidade > 1:
            print(f"E {contidade} pessoas tem mais de 18 anos.")
        else:
            print(f"E {contidade} pessoa tem mais de 18 anos.")
        break


    
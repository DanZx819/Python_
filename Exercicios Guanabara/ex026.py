frase = input("Digite algo: ").strip()

Maiuscula = frase.upper()
primeira = Maiuscula.find('A')
ultima = Maiuscula.rfind('A')
contar = Maiuscula.count('A')

print(f"""A frase ({frase}.)
Possui {contar} letras A
A primeira aparição da letra A foi no caractere {primeira}
E a ultima aparição foi no caractere {ultima}""")
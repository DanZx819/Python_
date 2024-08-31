import emoji
nome = input("Digite o seu nome completo: ")

lista = nome.split()

print(emoji.emojize(f"""Muito prazer em te conhecer!
O seu Primeiro nome: {lista[0]}  
E o seu Segundo nome: {lista[-1]}
:face_with_open_mouth::face_with_open_mouth::face_with_open_mouth:"""))
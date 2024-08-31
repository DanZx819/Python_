
cidade = input("Digite o nome de uma cidade: ")

C = cidade.upper()
procura = C.find('SANTO')

if procura == 0:
    print("O nome desta cidade começa com Santo")
else:
    print("O nome da cidade não começa com  Santo.")

listaaberto =[]
listafechado = []

ex = str(input("Digite uma expressão: "))
for p in ex:
    if p == '(':
        listaaberto.append(p)
    if p == ")":
        listafechado.append(p)

if len(listaaberto) == len(listafechado):
    print("Operação valida!")
else:
    print("Operação inválida!")
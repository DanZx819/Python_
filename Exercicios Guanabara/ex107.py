from uteis import números

num = int(input("Digite umm número: "))
fat = números.fatorial(num)
print(f"O fatorial do {num} é igual a {fat}")
print(f"O dobro de {num} é {números.dobro(num)}")
import math

co = float(input("Digite o Cateto Oposto: "))
ca = float(input("Digite o Cateto Adjacente: "))

co2 = pow(co, 2)
ca2 = pow(ca, 2)

h = co2 + ca2 #Soma dos catetos

h2 = math.sqrt(h)#Raiz Quadrada

print(f"Hipotenusa = {round(h2, 2)}")
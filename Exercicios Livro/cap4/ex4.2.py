n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(f"Maior número {n1}")
if n2 > n1 and n2 > n3:
    print(f"Maior número {n2}")
if n3 > n1 and n3 > n2:
    print(f"Maior número {n3}")

if n1 < n2 and n1 < n3:
    print(f"Menor número {n1}")
if n2 < n1 and n2 < n3:
    print(f"Menor número {n2}")
if n3 < n1 and n3 < n2:
    print(f"Menor número {n3}")
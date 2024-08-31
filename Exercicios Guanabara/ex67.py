n = 0

while True:
    print("-"*40)
    n = int(input("Você quer ver a tabuada de qual números: "))
    print("-"*40)
    if n < 0:
        print("Programa Encerrado!!!")
        print("-"*40)
        break
    for c in range(1 , 11):
        print(f"{n} x {c} = {n*c}")



num = int(input("Digite um numero: "))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f"{c} é divisivel")
        primo = primo + 1
    else:
        print(f"{c} não é divisivel")

if primo == 2:
    print("Ele é um numero primo")
else:
    print("Ele não é um numero primo")        
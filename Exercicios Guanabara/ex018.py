import random
import time

nome1 = str("Daniel")
nome2 = str("Martins")
nome3 = str("Grosso")
nome4 = str("Gonçalves")
print(f"O professor esta escolhendo um aluno para apagar a lousa...")
time.sleep(3)
s = random.randint(1, 4)

if s == 1:
    print(f"O {nome1} vai apagar a lousa")
elif s == 2:
    print(f"O {nome2} vai apagar a lousa")
elif s == 3:
    print(f"O {nome3} vai apagar a lousa")
elif s == 4:
    print(f"O {nome4} vai apagar a lousa")

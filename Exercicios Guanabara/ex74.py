
import random

turpla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))

print(f"Eu sortei ", end='')
for c in turpla:
    print(f"{c} -> ", end='')    
print("Terminei")
print(f"O maior número foi {max(turpla)} e o menor foi {min(turpla)}")




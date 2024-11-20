import random

array = []
for _ in range(10):
    random_cislo = random.randint(0, 100)
    array.append(random_cislo)

print("Pole:", array)

array1 = sorted(array)
print("Jednoduchý sort:", array1)

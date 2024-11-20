import random

array = []
for _ in range(10):
    random_cislo = random.randint(0, 100)
    array.append(random_cislo)

print("Pole:", array)

array1 = sorted(array)
print("Jednoduchý sort:", array1)


array3 = [10,54,575,45,4752,7,547862,8325785,47,42,47,12,4,4,2,4,2,1,4,5,54,654,1,35,465,43,51,6846,457]

def bubble_sort ():
    n = len(array3)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array3[j] > array3[j+1]:
                array3[j+1], array3[j] = array3[j], array3[j+1]
                print(array3)
    return array3

print(bubble_sort())

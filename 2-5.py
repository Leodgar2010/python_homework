# Реализуйте алгоритм перемешивания списка.
from random import randint

a_lenght = int(input("Введите длину списка: "))
a = []
for i in range(a_lenght):
    a.append(int(input("Введите элемент списка: ")))
print(a)
for i in range(0, len(a)):
    j = randint(0, len(a) - 1)
    print(j)
    a[i], a[j] = a[j], a[i]
print(a)

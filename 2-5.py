# Реализуйте алгоритм перемешивания списка.
from random import Random, random


list_lenght = int (input ("Введите длину списка: "))
list = []
result = []
for i in range (list_lenght):
    list.append (input ("Введите элемент списка: "))
print (list)
Random.sample (list, result)
print (result)

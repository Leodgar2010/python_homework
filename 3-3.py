# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт
# разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from source import create_list_float as clf
lst = clf()
lst2 = []
for i in range (len(lst)):
   lst2.append (round (lst [i]- int(lst[i]),2))
print (round (max(lst2)-min(lst2),2))


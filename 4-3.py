# Задайте последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов
# исходной последовательности
from source import create_random_list as cl
lst = cl(10,1)
print (lst)
count = 0
result = []
for i in lst:
    for j in lst:
        if j == i:
            count +=1
    if count <2:
        result.append (i)
    count = 0
print (sorted (result))
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from source import create_list_int as cl

lst = cl()
result = 0
for i in range(1, len(lst), 2):
    result = result + lst[i]
print(result)

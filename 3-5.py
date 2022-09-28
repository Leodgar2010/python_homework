# Задайте число. Составьте список
# чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# для k = 8 список будет
# выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from source import fib

num = int(input("Введите число: "))
list = []
i = 1
for e in range(1, num + 1):
    a = (i * (fib(e)))
    list.append(a)
    i = i * -1
list = list[::-1]
list.append(0)
for e in range(1, num + 1):
    list.append(fib(e))
print(list)

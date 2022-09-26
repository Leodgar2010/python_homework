# Задайте список из n чисел последовательности
# (1+1/n)^n выведите на экран их сумму
n = int(input("Введите число: "))
a = 0
list = []
for i in range(1, n + 1):
    a = round((1 + (1 / i)) ** i, 2)
    list.append(a)
print(list)
print(sum(list))

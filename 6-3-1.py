# Измените код одной-двух решенных
# ранее задач (с прошлых семинаров или
# домашних работ), применив лямбды, filter,
# map, zip, enumerate, списочные выражения.

# import random
#
# number_len = 10
# number = int((round(random.random(), number_len)) * (10 ** number_len))
# print(number)
# lst = []
# for i in range(len(str(number))):
#     lst.append(str(number)[i])
# print(f"Большее число: {max(lst)} Меньшее число: {min(lst)}")
import random

number_len = 10
number = int((round(random.random(), number_len)) * (10 ** number_len))
print(number)
lst = [i for i in range(len(str(number)))]
print(f"Большее число: {max(lst)} Меньшее число: {min(lst)}")

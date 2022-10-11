# Измените код одной-двух решенных
# ранее задач (с прошлых семинаров или
# домашних работ), применив лямбды, filter,
# map, zip, enumerate, списочные выражения.

# Дан список чисел. Выведите все элементы
# списка, которые больше предыдущего элемента
# lst = [1,3,2,5,4,6]
# result = []
# for i in range (1,len(lst)):
#     if lst [i] > lst [i-1]:
#         result.append (lst [i])
# print (result)

lst = [1, 3, 2, 5, 4, 6]
print(list(filter(lambda x: x > lst[lst.index(x) - 1], lst)))

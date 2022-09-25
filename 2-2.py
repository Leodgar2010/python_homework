# Напишите программу, которая
# принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
a = int(input("Введите число: "))
list = []
count = 0
for i in range(1, a + 1):
    if i == 1:
        list.append(i)
    else:
        list.append(i * list[count - 1])
    count += 1
print(list)

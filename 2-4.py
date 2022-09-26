# Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.
import os

n = int(input("Введите число: "))
list = []
for i in range(-n, n):
    list.append(i)
print(list)
a = open('file.txt', 'w')
a.write((input("Введите первую позицию: ")))
a.write("\n")
a.write(input("Введите вторую позицию: "))
a.close()
a = open('file.txt', 'r')
print(list[int(a.read(1))] * list[int(a.read(3))])
a.close()
os.remove("file.txt")


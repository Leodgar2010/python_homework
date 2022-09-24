# Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input("Введите число: "))
list = []
for i in range (-n,n): 
    list.append (i)
print (list)
open ("C:\Users\pnsmi\YandexDisk\Учёба\Python\Homework\file.txt")

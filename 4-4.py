# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
from source import create_polinom
a = (int(input ("Введите степень: ")))
file1 = open ('4-5-2.txt', 'w')
file1.write (create_polinom(a,2))
file1.close()



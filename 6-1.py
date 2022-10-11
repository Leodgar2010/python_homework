# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b),
# возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель
# для списка натуральных чисел. Ввод чисел продолжается
# до ввода пустой строки.
import math


def create_users_list():
    result = []
    while True:
        a = (input('Введите число '))
        if a == "":
            break
        else:
            result.append(int(a))
    return result


def gcd_max_lst(lst):
    print(lst)
    gcd_max = 0
    result = []
    for i in lst:
        for j in lst:
            if i != j:
                gcd_max = math.gcd(i, j)
            if (gcd_max not in result) and (gcd_max != 0):
                result.append(gcd_max)
    return result


lst = (create_users_list())
print(lst)
print('Наибольший общий делитель: ', min(gcd_max_lst(lst)))

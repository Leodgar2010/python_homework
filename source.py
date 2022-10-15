# def create_list_int():
#     a_lenght = int(input("Введите длину списка: "))
#     a = []
#     a = [i for i in range(a_lenght):a.append(int(input("Введите элемент списка: "))]
#     return (a)


def create_list_float():
    a_lenght = int(input("Введите длину списка: "))
    a = []
    for i in range(a_lenght):
        a.append(float(input("Введите элемент списка: ")))
    return (a)


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def create_random_list (list_lenght,number_lenght):
    from random import random
    lst = []
    for i in range(0, list_lenght):
        lst.append(int((round((random()), number_lenght)) * (10**number_lenght)))
    return(lst)
def create_polinom (power, coeff_lenght):
    from source import create_random_list
    lst = create_random_list(power+1,coeff_lenght)
    result = None
    for i in range (0, len(lst)):
        if result == None:
            result = (f"{lst[i]}*(x**{power-i})")
        else:
            if (power-i) > 1:
                result = result + '+' + (f"{lst[i]}*(x**{power - i})")
            elif (power-i) == 1:
                result = result +'+'+ (f"{lst[i]}*x")
            else:
                result = result +'+'+ (f"{lst[i]}")
    return (result)
def create_polinom_sum_from_file(file1, file2, sum_file):
    a = (open(file1, 'r').readline())
    b = (open(file2, 'r').readline())
    alst = a.split('+')
    blst = b.split('+')
    clst = []
    temp = []
    for i in range(len(alst)):
        alst1 = alst[i].split("*")
        blst1 = blst[i].split("*")
        temp.append(str(int(alst1[0]) + int(blst1[0])))
        temp = temp + alst1[1:]
        clst.append("*".join(temp))
        temp = []
    result = "+".join(clst)
    text = open(sum_file, 'w')
    text.writelines(result)
    text.close()






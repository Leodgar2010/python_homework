def create_list_int():
    a_lenght = int(input("Введите длину списка: "))
    a = []
    for i in range(a_lenght):
        a.append(int(input("Введите элемент списка: ")))
    return (a)


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




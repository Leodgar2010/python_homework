# Реализуйте RLE алгоритм: реализуйте
# модуль сжатия и восстановления данных.
text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"


def arhive(text):
    count = 0
    lst = []
    for i in range(0, len(text)):
        temp = text[i:i + 1]
        lst.append(temp)
    result = [lst[0]]
    quantity = 0
    for i in range(len(lst) + 1):
        if (i) == len(lst):
            result.append(str(quantity))
            break
        elif lst[i] == result[count]:
            quantity += 1
        elif i < len(lst):
            result.append(str(quantity))
            quantity = 1
            result.append(lst[i])
            count += 2
    return result


def unarhive(lst):
    result = str()
    for i in range(1, len(lst), 2):
        result = result + (lst[i - 1] * (int(lst[i])))
    return (result)


text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
print(text)
a = arhive(text)
print("".join(a))
b = unarhive(a)
print(b)

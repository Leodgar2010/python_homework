# Создайте программу для игры в ""Крестики-нолики"".
field = [i for i in range(1, 10)]
print(f"{field[:3]}\n{field[3:6]} \n{field[6:]}")
while True:
    a = int(input("Первый игрок выберите позицию для крестика "))
    field.remove(a)
    field.insert(a - 1, "X")
    print(f"{field[:3]}\n{field[3:6]} \n{field[6:]}")
    b = int(input("Второй игрок выберите позицию для нолика "))
    field.remove(b)
    field.insert(b - 1, "0")
    print(f"{field[:3]}\n{field[3:6]} \n{field[6:]}")
    c = (input("Кто-то подбедил (yes/no)? "))
    if c == "yes":
        break
    elif c == "no":
        continue
    else:
        print("Будем считать, что это ничья")
        break

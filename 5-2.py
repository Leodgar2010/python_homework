# Создайте программу для игры с
# конфетами человек против человека.
# Условие задачи: На столе лежит 2021
# конфета. Играют два игрока делая
# ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
def candy_take_game(candys):
    while True:
        candy_take = int(input("Сколько конфет вы хотите забрать? "))
        if candy_take > 28:
            print("Вы взяли слишком много конфет. Максимум 28.")
        elif candys < 0:
            print(f"Вы могли взять только {candy_take + candys} конфет.")
        else:
            break
    return candy_take


def candy_take_bot(candys):
    from random import randint
    candy_take = randint(1, 28)
    if candy_take > candys:
        candy_take = candys
    print(candy_take)
    return candy_take


def candy_take_clever_bot(candys):
    candy_take = candys - int(candys / 29) * 29
    if candy_take > 28 or candy_take == 0:
        candy_take = 1
    elif candys <= 28:
        candy_take = candys
    print(candy_take)
    return candy_take


candys = 2021
candy_take = 0
flag = True
while candys != 0:
    if flag == True:
        print("Ход первого игрока")
        candy_take = candy_take_clever_bot(candys)
    if flag == False:
        print("Ход второго игрока")
        candy_take = candy_take_bot(candys)
    if flag == True:
        flag = False
    else:
        flag = True
    candys = candys - candy_take
    print(f"Осталось {candys} конфет")

    if candys == 0:
        if flag == True:
            print("Второй игрок победил и забрал все конфеты")
        else:
            print("Первый игрок победил и забрал все конфеты")

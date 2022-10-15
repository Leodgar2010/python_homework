# Создайте программу для игры в ""Крестики-нолики"".
def TicTacToesWinner (field):
    check =[]
    for i in range (5):
        check.append ([])
    for i in range(len(field)):
        for j in range(len (field)):
            check [i].append (field [j][i])
    check[3] =([field [0][0],field [1][1],field [2][2]])
    check[4] = ([field[0][2], field[1][1], field[0][2]])
    for i in range (len(field)):
        check.append (field[i])
    print (check)
    result = str()
    for i in check:
        print (i[0],i[1],i[2])
        if i[0]==i[1]==i[2]:
            result = (f"Победа {i[0]}"a)
            break
        else:
            result = ('Никто не победил')
    return result






# field = [[1,2,3],[4,5,6],[7,8,9]]
field = [['X',2,3],[4,'X',6],[7,9,'X']]
print (TicTacToesWinner(field))
# print(f"{field[0]}\n{field[1]} \n{field[2]}")
# while True:
#     a = int(input("Первый игрок выберите позицию для крестика "))
#     for i in field:
#         for j in range (len(i)):
#             if a == i[j]:
#                 i.insert(j, "X")
#                 i.remove(a)
#     print(f"{field[0]}\n{field[1]} \n{field[2]}")
#     b = int(input("Второй игрок выберите позицию для нолика "))
#     for i in field:
#         for j in range(len(i)):
#             if b == i[j]:
#                 i.insert(j, "0")
#                 i.remove(b)
#     print(f"{field[0]}\n{field[1]} \n{field[2]}")
#     TicTacToesWinner(field, 'X')

    # c = (input("Кто-то подбедил (yes/no)? "))
    # if c == "yes":
    #     break
    # elif c == "no":
    #     continue
    # else:
    #     print("Будем считать, что это ничья")
    #     break

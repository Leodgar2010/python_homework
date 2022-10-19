def show_main_menu():
    return int(input ("1 - создать новую базу данных \n2 - открыть существующую базу данных \n"))
def show_choosing_action_menu ():
    return int(input ("1 - добавить данные \n2 - удалить данные \n"))
def show_add_data_menu():
    return int (input("1 - добавить новую колонку\n2 - добавить новую сроку\n3 - добавить данные в ячейку\n"))
def show_delete_data_menu ():
    return int(input("1 - удалить целую колонку\n2 - удалить целую строку\n3 - удалить данные в ячейке\n"))
def name_file ():
    return input ("Введите название файла ")
def name_new_column():
    return str(input ("Введите наименование новой колонки "))
def invite_fill_row ():
    return (input("Введите данные для каждой колонки через пробел, если в колонке нет данных поставьте прочерк '-' ")).split()
def invite_choose_cell():
    return (input("Введите название колонки и индекс строки ячейки через пробел ")).split()
def name_cell ():
    return input ("Введите данные для ячейки ")
def invite_delete_row():
    return int(input("Введите индекс строки для удаления "))
def invite_delete_column():
    return (input("Введите наименование колонки для удаления "))
def check_input_end():
    while True:
        temp = input("Ввод данных закончен? (Да/Нет) ")
        if temp.lower() == 'да':
            flag = False
            break
        elif temp.lower() == 'нет':
            flag = True
            break
        else:
            print("Вы не ввели ни Да ни Нет")
    return flag


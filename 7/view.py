def recieve_data_surname():
    return (input("Введите фамилию: "))


def recieve_data_name():
    return (input("Введите имя: "))


def recieve_data_phone_number():
    return (input("Введите номер телефона: "))


def recieve_data_comment():
    return (input("Введите комментарий: "))


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


def check_file_format():
    while True:
        result = int(input('Выберите формат файла:\n1 - *.txt\n2 - *.csv\n3 - *.txt и *.csv\n\n'))
        if result < 0 or result > 3:
            print("Вы ввели неверное число")
        else:
            break
    return result

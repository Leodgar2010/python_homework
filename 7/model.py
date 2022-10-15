import view


def form_data_source():
    surname = view.recieve_data_surname()
    name = view.recieve_data_name()
    phone_number = view.recieve_data_phone_number()
    comment = view.recieve_data_comment()
    return [surname, name, phone_number, comment]


def form_index_txt(lst):
    index = open('index.txt', 'a', encoding='utf-8')
    for i in range(len(lst)):
            index.writelines(f"{lst[i]}\n\n")


def form_index_csv(lst):
    import csv
    with open("index.csv", mode="a",encoding='windows-1251') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_writer.writerow([lst[0], lst[1], lst[2], lst[3]])

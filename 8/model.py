import csv


def csv_data_create(file, lst):
    with open(file, "w", encoding="windows-1251", newline='') as file:
        writer = (csv.writer(file, delimiter=';', ))
        writer.writerow(lst)


def csv_create_with_lst(file, lst):
    csv_data_create(file, lst[0])
    for i in lst[1:]:
        csv_add_info(file, i)


def csv_create_column(file, name):
    lst = csv_data_open(file)
    lst[0].insert(len(lst[0]), name)
    for i in lst[1:]:
        i.append("-")
    csv_create_with_lst(file, lst)


def csv_data_open(file):
    with open(file, encoding="windows-1251") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        return list(reader)


def csv_add_info(file, list):
    with open(file, 'a', encoding="windows-1251", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(list)


def csv_delete_info(file, del_info):
    with open(file, encoding="windows-1251", newline="") as file:
        reader = list(file.reader(file, delimiter=';'))
        for i in reader:
            if del_info in reader: reader.remove(i)


def csv_add_cell_info(file, lst_cell, cell):
    lst_file = csv_data_open(file)
    x = lst_file[0].index(lst_cell[0])
    lst_file[int(lst_cell[1])].pop(x)
    lst_file[int(lst_cell[1])].insert(x, cell)
    csv_data_create(file, lst_file[0])
    for i in lst_file[1:]:
        csv_add_info(file, i)


def print_with_enumerate(file):
    lst = (csv_data_open(file))
    for i, row in enumerate(lst):
        print(i, " ".join(row))

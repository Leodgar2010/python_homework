import model
import view


def start():
    temp = view.show_main_menu()
    flag = True
    file = (f"{view.name_file()}.csv")
    if temp == 1:
        lst = (view.invite_fill_row())
        model.csv_data_create(file, lst)
        print (lst)
        while flag:
            lst = (view.invite_fill_row())
            model.csv_add_info(file, lst)
            flag = view.check_input_end()
        model.print_with_enumerate(file)
    elif temp==2:
        temp=view.show_choosing_action_menu()
        model.print_with_enumerate(file)
        if temp==1:

            temp=view.show_add_data_menu()
            if temp==1:
                name = view.name_new_column()
                model.csv_create_column (file,name)
            elif temp==2:
                lst = (view.invite_fill_row())
                model.csv_add_info(file,lst)
            else:
                lst_cell = (view.invite_choose_cell())
                cell = view.name_cell()
                model.csv_add_cell_info (file,lst_cell,cell)
        if temp==2:
            temp=view.show_delete_data_menu()
            model.print_with_enumerate(file)
            if temp==1:
                del_info = (view.invite_delete_column ())
                lst = model.csv_data_open(file)
                x = lst[0].index(del_info)
                for i in lst:
                    i.pop(x)
                model.csv_create_with_lst(file,lst)
            elif temp==2:
                del_info = (view.invite_delete_row ())
                lst = model.csv_data_open(file)
                lst.pop (del_info)
                model.csv_create_with_lst(file,lst)
            else:
                model.print_with_enumerate(file)
                lst_cell = (view.invite_choose_cell())
                model.csv_add_cell_info(file, lst_cell, "-")






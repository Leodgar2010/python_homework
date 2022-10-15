import model
import view


def start():
    temp = view.check_file_format()
    flag = True
    if temp == 1:
        while flag:
            lst = model.form_data_source()
            model.form_index_txt(lst)
            flag = view.check_input_end()
    if temp == 2:
        while flag:
            lst = model.form_data_source()
            model.form_index_csv(lst)
            flag = view.check_input_end()
    if temp == 3:
        while flag:
            lst = model.form_data_source()
            model.form_index_txt(lst)
            model.form_index_csv(lst)
            flag = view.check_input_end()

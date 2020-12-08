def check_sum(spisok_chisel, summa):
    my_dict_tmp = {}
    for i in spisok_chisel:
        if my_dict_tmp.setdefault(i) is None:
            my_dict_tmp[summa - i] = True
        else:
            return my_dict_tmp[i]


check_sum([1, 3, 2, 12, 11], 5)

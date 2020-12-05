def check_sum(spisok_chisel, summa):
    for i in spisok_chisel:
        for k in spisok_chisel:
            if i + k == summa:
                return True


check_sum([1, 3, 2, 12, 11], 5)

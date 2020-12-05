def check_sum(spisok_chisel, summa):
    for i in range(len(spisok_chisel)):
        if spisok_chisel[i] + spisok_chisel[i + 1] == summa:
            return True


check_sum([1, 3, 2, 12, 11], 5)

def check_sum(spisok_chisel, summa):
    for i in range(len(spisok_chisel) - 1):
        for k in range(i + 1, len(spisok_chisel)):
            if spisok_chisel[i] + spisok_chisel[k] == summa:
                return True


check_sum([1, 3, 2, 12, 11], 5)

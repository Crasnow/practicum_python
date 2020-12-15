def number_translation(number, rank=1):
    result = ''

    if rank <= 0:
        print("Введите существую систему счисления.")
        return

    while number >= rank:
        temp_number = number // rank
        result += str(number - temp_number * rank)
        number = temp_number
    result += str(number)

    return result[::-1]

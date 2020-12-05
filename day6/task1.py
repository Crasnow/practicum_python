def check_number(number):
    number_string = str(number)

    if int(number_string[0]) == int(number_string[1]) or int(number_string[0]) + int(number_string[1]) == 10:
        return True
    return False

def number_translation(number):
    result = ''

    while number >= 2:
        temp_number = number // 2
        result += str(number - temp_number * 2)
        number = temp_number
    result += str(number)

    return result[::-1]

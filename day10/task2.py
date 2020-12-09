def number_translation(number, rank):
    result = ''

    while number >= rank:
        temp_number = number // rank
        result += str(number - temp_number * rank)
        number = temp_number
    result += str(number)

    return result[::-1]

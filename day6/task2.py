def check_number(number):
    number_string = str(number)
    count = 0
    even_list = []
    odd_list = []
    even_sum = 0
    odd_sum = 0
    flag = True

    for i in number_string:
        count += 1
        if count % 2 == 0:
            even_list.append(int(i))
        else:
            odd_list.append(int(i))

    for i in range(len(even_list)):
        odd_sum += odd_list[i]
        even_sum += even_list[i]
        if odd_list[i] != even_list[i]:
            flag = False

    if even_sum == odd_sum or flag == True:
        return True
    return False

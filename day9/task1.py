trigger_win = 'Ничья'
count = 0



def print_game_field(field):
    for j in range(3):
        for l in range(3):
            print(field[j][l], end='')
        print()


def test(count, game_field=[['* ' for i in range(3)] for k in range(3)], number_game_field = [[0 for i in range(3)] for k in range(3)],flag=False):
    if count % 2 != 0:
        v = input("Введите координаты через пробел: ").split()
        x = int(v[0]) - 1
        y = int(v[1]) - 1

        game_field[x][y] = 'X '
        number_game_field[x][y] = 1
        count += 1

    else:
        for x in range(3):
            for y in range(3):
                if number_game_field[x][y] == 0 and flag == False:
                    number_game_field[x][y] = -1
                    game_field[x][y] = '0 '
                    count += 1
                    flag = True


while count != 9:
    test(count)

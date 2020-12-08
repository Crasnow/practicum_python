number_pole = [[0 for i in range(3)] for k in range(3)]
pole = [['* ' for i in range(3)] for k in range(3)]
win = 'Ничья'
n = 0
flag = False

z = input("Введите чем, будете играть: 0 или Х: ")
if z[0] in ['X', 'x', 'Х', 'х']:
    while n != 9:

        if n % 2 == 0:
            v = input("Введите координаты через пробел: ").split()
            x = int(v[0]) - 1
            y = int(v[1]) - 1

            pole[x][y] = 'X '
            number_pole[x][y] = 1
            n += 1

        else:
            for x in range(3):
                for y in range(3):
                    if number_pole[x][y] == 0 and flag == False:
                        number_pole[x][y] = -1
                        pole[x][y] = '0 '
                        n += 1
                        flag = True

        for i in number_pole:
            if sum(i) == 3:
                win = 'Победа крестиков'
                n = 9
            if sum(i) == -3:
                win = 'Победа ноликов'
                n = 9

        for i in range(3):
            s = 0
            for k in range(3):
                s += number_pole[k][i]
            if s == 3:
                win = 'Победа крестиков'
                n = 9
            if s == -3:
                win = 'Победа ноликов'
                n = 9

        s = 0
        for i in range(3):
            s += number_pole[i][i]
        if s == 3:
            win = 'Победа крестиков'
            n = 9
        if s == -3:
            win = 'Победа ноликов'
            n = 9

        s = 0
        for i in range(3):
            s += number_pole[i][2 - i]
        if s == 3:
            win = 'Победа крестиков'
            n = 9
        if s == -3:
            win = 'Победа ноликов'
            n = 9

        if n % 2 == 0 and win == 'Ничья':
            for j in range(3):
                for l in range(3):
                    print(pole[j][l], end='')
                print()
            flag = False

    for j in range(3):
        for l in range(3):
            print(pole[j][l], end='')
        print()
    flag = False
    print(win)

if z[0] == '0':
    while n != 9:

        if n % 2 != 0:
            v = input("Введите координаты через пробел: ").split()
            x = int(v[0]) - 1
            y = int(v[1]) - 1

            pole[x][y] = '0 '
            number_pole[x][y] = 1
            n += 1

        else:
            for x in range(3):
                for y in range(3):
                    if number_pole[x][y] == 0 and flag == False:
                        number_pole[x][y] = -1
                        pole[x][y] = 'X '
                        n += 1
                        flag = True

        for i in number_pole:
            if sum(i) == 3:
                win = 'Победа крестиков'
                n = 9
            if sum(i) == -3:
                win = 'Победа ноликов'
                n = 9

        for i in range(3):
            s = 0
            for k in range(3):
                s += number_pole[k][i]
            if s == 3:
                win = 'Победа крестиков'
                n = 9
            if s == -3:
                win = 'Победа ноликов'
                n = 9

        s = 0
        for i in range(3):
            s += number_pole[i][i]
        if s == 3:
            win = 'Победа крестиков'
            n = 9
        if s == -3:
            win = 'Победа ноликов'
            n = 9

        s = 0
        for i in range(3):
            s += number_pole[i][2 - i]
        if s == 3:
            win = 'Победа крестиков'
            n = 9
        if s == -3:
            win = 'Победа ноликов'
            n = 9

        if n % 2 == 0 and win == 'Ничья':
            for j in range(3):
                for l in range(3):
                    print(pole[j][l], end='')
                print()
            flag = False

    for j in range(3):
        for l in range(3):
            print(pole[j][l], end='')
        print()
    flag = False
    print(win)


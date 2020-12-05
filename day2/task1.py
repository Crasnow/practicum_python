text = input('Введите текст: ')
number = int(input('Введите максимальную длину: '))

print(len(text), len(''.join(text.split())))

if len(text) % 2 == 0:
    print('количество символов в тексте четное')
elif len(text) % 2 != 0:
    print('количество символов в тексте нечетное')
else:
    print('не удалось определить четность символов в тексте. Количество символов: ' + len(text))

if len(text) > number:
    print(f'длина текста превышает длину {number} символов')

note = input().split(',')


def split_words(dict, separator):
    tmp_dict = []
    for i in dict:
        split_dict = i.split(separator)
        for j in split_dict:
            tmp_dict.append(j)

    dict.clear()
    for k in tmp_dict:
        if k != '':
            dict.append(k)

    return dict


split_words(note, ' ')
print(note)

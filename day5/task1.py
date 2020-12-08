key_encript = [91, 65, 123, 97, 1]
key_decipher = [64, 90, 96, 122, -1]


def cryptologic(key, letter):
    if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
        letter = chr(ord(letter) + key[4])
        if ord(letter) == key[0]:
            letter = chr(key[1])
        if ord(letter) == key[2]:
            letter = chr(key[3])
        letter = change_letters_case(letter)
    return letter


def change_letters_case(letter):
    if letter == letter.upper():
        letter = letter.lower()
    else:
        letter = letter.upper()
    return letter


def encript(text):
    encript_text = ''

    for i in text:
        i = cryptologic(key_encript, i)
        encript_text += i

    return encript_text


def decipher(text):
    decipher_text = ''

    for i in text:
        i = cryptologic(key_decipher, i)
        decipher_text += i

    return decipher_text

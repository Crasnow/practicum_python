def encript(text):
    encript_text = ''

    for i in text:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            i = chr(ord(i) + 1)
            if ord(i) == 91:
                i = chr(65)
            if ord(i) == 123:
                i = chr(97)
            if i == i.lower():
                i = i.upper()
            else:
                i = i.lower()
        encript_text += i
    return encript_text


def decipher(text):
    decipher_text = ''

    for i in text:
        if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
            i = chr(ord(i) - 1)
            if ord(i) == 64:
                i = chr(90)
            if ord(i) == 96:
                i = chr(122)
            if i == i.upper():
                i = i.lower()
            else:
                i = i.upper()
        decipher_text += i
    return decipher_text

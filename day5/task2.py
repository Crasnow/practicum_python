import hashlib
import uuid


def hash_text(text):
    salt = uuid.uuid4().hex
    hash = hashlib.md5(text.encode('utf-8')).hexdigest() + salt

    with open('bd.txt', 'a') as f:
        f.write(f'{text}|{salt}|{hash}' + '\n')
    return f


def find_salt_text(hash):
    result = {}
    with open('bd.txt', 'r') as f:
        for line in f:
            if hash + '\n' == line.split('|')[2]:
                result['Text'] = line.split('|')[0]
                result['Salt'] = line.split('|')[1]
                return result
        print(f'По данному хэшу {hash} не найдены записи.')


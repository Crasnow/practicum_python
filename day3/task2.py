import re
import json

new_text = input()
count_words = int(input())
symbols = '[,|!|?|.]'

clear_text_symbols = (re.sub(symbols, '', new_text).lower()).split(' ')
clear_text_double = set()
dict_words = {}

for i in clear_text_symbols:
    clear_text_double.add(i)

for i in clear_text_double:
    count = clear_text_symbols.count(i)

    if count >= count_words:
        dict_words[i] = count

parasite_words_json = json.dumps(dict_words, ensure_ascii=False)

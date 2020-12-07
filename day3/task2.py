import re
import json

text = input()
count_words = int(input())
symbols = '[,|!|?|.]'

text_as_set_wo_symbols = (re.sub(symbols, '', text).lower()).split(' ')
text_as_set_wo_doubles = set()
dict_words = {}

for i in text_as_set_wo_symbols:
    text_as_set_wo_doubles.add(i)

for i in text_as_set_wo_doubles:
    count = text_as_set_wo_symbols.count(i)

    if count >= count_words:
        dict_words[i] = count

parasite_words_json = json.dumps(dict_words, ensure_ascii=False)

print(count)


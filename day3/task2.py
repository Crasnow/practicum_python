import re
import json

text = input()
count_words = int(input())
symbols = '[,|!|?|.]'

text_as_set_wo_symbols = (re.sub(symbols, '', text).lower()).split(' ')
text_as_set_wo_doubles = {}
result = {}

for i in text_as_set_wo_symbols:
    if text_as_set_wo_doubles.setdefault(i) is None:
        text_as_set_wo_doubles[i] = 1
    else:
        text_as_set_wo_doubles[i] = text_as_set_wo_doubles.setdefault(i) + 1

    if text_as_set_wo_doubles.setdefault(i) >= count_words:
        result[i] = text_as_set_wo_doubles.setdefault(i)

parasite_words_json = json.dumps(result, ensure_ascii=False)

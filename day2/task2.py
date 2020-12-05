import json


def change_word(orig_txt, old_words, new_word):
    tmp_text = orig_txt
    for i in old_words:
        pure_text = tmp_text.replace(i, new_word)
        tmp_text = pure_text
    return pure_text


text = input('Введите текст: ')
max_len = int(input('Введите максимальную длину: '))
forbidden_words = ["волшебники", "Гарри Поттер"]
analytic_txt = {'length': len(text),
                'pure_length': len(''.join(text.split())),
                'origin_text': text,
                'pure_text': change_word(text, forbidden_words, "***"),
                'pure_short_text': text[0:max_len + 1] + '...'}

analytic_txt_json = json.dumps(analytic_txt, ensure_ascii=False)

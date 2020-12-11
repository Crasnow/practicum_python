from random import randint


def magic_ball(question=''):
    question = input("Введите свой вопрос: ")
    answers = ["Да", "Нет", "Вряд ли", "Не надейся", "Очень скоро", "Точно",
               "Спроси снова", "Так тому и быть", "Абсолютно точно", "Звезды говорят нет",
               "Духи говорят да", "Думаю да", "Не сейчас", "Не могу сказать", "Задай другой вопрос"]
    answer_for_you = answers[randint(0, len(answers) - 1)]

    if question == "Конец":
        print("Прощайте..")
        return

    if len(question) > 0:
        print(answer_for_you)
        magic_ball()
    if len(question) == 0:
        print("Не могу читать мысли. Напиши свой вопрос.")
        magic_ball()


magic_ball()

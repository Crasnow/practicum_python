import requests

request = requests.get('https://timezoneapi.io/api/ip/?token=anjXWCvwVzOdjzDaNmTJ')
time_hours = int(str(request.json()['data']['datetime']['time'])[0:2])
username = input("Введите ваше имя: ")

if 0 <= time_hours <= 4:
    print("Доброй ночи, " + username)
elif 5 <= time_hours <= 9:
    print("Доброе утро, " + username)
elif 10 <= time_hours <= 16:
    print("Добрый день, " + username)
elif 17 <= time_hours <= 23:
    print("Добрый вечер, " + username)
else:
    print("Не удалось определить время. Сейчас " + time_hours + " часов.")

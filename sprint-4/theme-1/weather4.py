import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    # Напишите тело этой функции.
    # Не изменяйте остальной код!
    try:
        req = requests.get(make_url(city=city), params=make_parameters())
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    except Exception as err:
        return '<ошибка на сервере погоды>'
    if req.status_code == 200:
        return req.text
    if int(req.status_code) // 100 == 4:
        return '<сетевая ошибка>'
    else:
        return '<ошибка на сервере погоды>'
      

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))

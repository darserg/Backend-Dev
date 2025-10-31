import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    '': ''
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url=url + '/Saratov?' + ''.join(weather_parameters))  # передайте параметры в http-запрос

print(response.text)
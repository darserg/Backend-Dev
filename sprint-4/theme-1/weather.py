import requests

url = 'http://wttr.in/Saratov?0T'

response = requests.get(url) # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа
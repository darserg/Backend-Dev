user_query = 'как стать бэкенд-разработчиком'
query = user_query.split()

url = 'https://yandex.ru/search/?text=' + '%20'.join(query)

print(url)
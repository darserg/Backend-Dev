# Импортируйте необходимые модули.
from datetime import datetime


# Укажите два параметра функции:
def validate_record(name, date_str):
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        print(f"Некорректный формат даты в записи: {name}, {date_str}")
        return False


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0

    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    for name, date_str in data:
        if validate_record(name, date_str):
            good_count += 1
        else:
            bad_count += 1

    return {"good": good_count, "bad": bad_count}


data = [
    ("Иван Иванов", "10.01.2004"),
    ("Пётр Петров", "15.03.1956"),
    ("Зинаида Зеленая", "6 февраля 1997"),
    ("Елена Ленина", "Второе мая тысяча девятьсот восемьдесят пятого"),
    ("Кирилл Кириллов", "26/11/2003"),
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
print(f"Корректных записей: {statistics['good']}")
print(f"Некорректных записей: {statistics['bad']}")

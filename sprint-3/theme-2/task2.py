# Импортируйте нужную библиотеку.
from datetime import datetime


class Store:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        # Метод is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        return False

    def get_info(self, date_str):
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        # Исправлен формат года с "%y" на "%Y" для четырехзначного года
        date_object = datetime.strptime(date_str, "%d.%m.%Y")

        # Передайте в метод is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.is_open(date_object):
            info = "работает"
        else:
            info = "не работает"
        return f"Магазин по адресу {self.address} {date_str} {info}"


class MiniStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        # Мини-маркеты работают только по будним дням (пн-пт)
        # weekday() возвращает: 0-пн, 1-вт, 2-ср, 3-чт, 4-пт, 5-сб, 6-вс
        return date.weekday() < 5  # Только понедельник-пятница


class WeekendStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        # Магазины выходного дня работают только по субботам и воскресеньям
        # weekday() возвращает: 0-пн, 1-вт, 2-ср, 3-чт, 4-пт, 5-сб, 6-вс
        return date.weekday() >= 5  # Только суббота и воскресенье


class NonStopStore(Store):
    # Переопределите метод is_open().
    def is_open(self, date):
        return True


# Тестирование
mini_store = MiniStore("Улица Немига, 57")
print(mini_store.get_info("29.03.2024"))  # Пятница - работает
print(mini_store.get_info("30.03.2024"))  # Суббота - не работает

weekend_store = WeekendStore("Улица Толе би, 321")
print(weekend_store.get_info("29.03.2024"))  # Пятница - не работает
print(weekend_store.get_info("30.03.2024"))  # Суббота - работает

non_stop_store = NonStopStore("Улица Арбат, 60")
print(non_stop_store.get_info("29.03.2024"))  # Любой день - работает
print(non_stop_store.get_info("30.03.2024"))  # Любой день - работает

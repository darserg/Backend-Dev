from datetime import datetime
from random import sample


def choose_days():
    # Определяем диапазон дат первой половины месяца.
    # Исправление: дни должны быть от 1 до 15 включительно
    first_month_half = list(range(1, 16))

    # Выбор трёх случайных чисел:
    random_days = sample(first_month_half, k=3)
    # Cортировка этих чисел по возрастанию:
    sorted_days = sorted(random_days)

    # Получаем сегодняшнюю дату.
    # На её основе будут генерироваться даты для занятий:
    now = datetime.now()

    # Чтобы было проще формировать сообщение, начнём цикл с 0.
    for i in range(3):
        # Генерируем дату занятия, подменяя номер дня в сегодняшней дате.
        # Исправление: используем правильный индекс из sorted_days
        # Исправление: формат месяца должен быть %m (месяц), а не %M (минуты)
        practice_day = now.replace(day=sorted_days[i]).strftime("%d.%m.%Y")
        print(f"{i+1}-е занятие: {practice_day}")


choose_days()

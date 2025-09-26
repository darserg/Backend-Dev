# Пропишите нужные импорты.
from datetime import datetime, timedelta


def get_weekday_name(weekday_number):
    weekdays = [
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    ]
    return weekdays[weekday_number]


def get_day_after_tomorrow(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    today_weekday = get_weekday_name(date.weekday())
    tomorrow = date + timedelta(days=2)
    tomorrow_weekday = get_weekday_name(tomorrow.weekday())
    print(
        "Сегодня "
        + date_string
        + ", "
        + str(today_weekday)
        + ", а послезавтра будет "
        + str(tomorrow_weekday)
    )


# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow("2024-01-01")
get_day_after_tomorrow("2024-01-02")
get_day_after_tomorrow("2024-01-03")
get_day_after_tomorrow("2024-01-04")
get_day_after_tomorrow("2024-01-05")
get_day_after_tomorrow("2024-01-06")

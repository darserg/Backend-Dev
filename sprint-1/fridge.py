import datetime
from decimal import Decimal

DATE_FORMAT = "%Y-%m-%d"

goods = {}


def add(items, title, amount, expiration_date=None):
    title = title.strip()
    amount = Decimal(str(amount))  # Преобразуем в Decimal

    # Преобразуем строку с датой в объект date, если указана
    exp_date = None
    if expiration_date is not None:
        exp_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    # Если товар уже есть — добавляем в существующий список партий
    if title in items:
        items[title].append({"amount": amount, "expiration_date": exp_date})
    else:
        # Иначе создаём новый список с одной партией
        items[title] = [{"amount": amount, "expiration_date": exp_date}]


def add_by_note(items, note):
    note = note.strip()
    if not note:
        raise ValueError("Заметка не может быть пустой.")

    parts = note.split()

    if len(parts) < 2:
        raise ValueError(
            f"Заметка должна содержать как минимум название и количество. Получено: {len(parts)} частей."
        )

    # Проверяем, является ли последняя часть датой
    expiration_date = None
    quantity_str = parts[-1]  # предполагаем, что последнее — количество
    title_parts = parts[:-1]  # всё остальное — название

    # Попробуем распарсить последнюю часть как дату
    try:
        datetime.datetime.strptime(parts[-1], DATE_FORMAT)
        # Если удалось — значит, последняя часть — дата, а количество — предпоследнее
        if len(parts) < 3:
            raise ValueError(
                f"Для указания даты должно быть минимум 3 части: название, количество, дата. Получено: {len(parts)}"
            )
        expiration_date = parts[-1]
        quantity_str = parts[-2]
        title_parts = parts[:-2]
    except ValueError:
        # Последняя часть — не дата → считаем, что это количество, дата не указана
        pass

    # Проверяем, что количество — число
    try:
        amount = Decimal(quantity_str)
    except:
        raise ValueError(f"'{quantity_str}' не является числом")

    # Собираем название
    title = " ".join(title_parts).strip()
    if not title:
        raise ValueError("Название продукта не может быть пустым.")

    # Вызываем add
    add(items, title, amount, expiration_date)


def find(items, needle):
    needle = needle.lower()
    result = []
    for title in items.keys():
        if needle in title.lower():
            result.append(title)
    return result


def amount(items, needle):
    found_titles = find(items, needle)
    total = Decimal("0")
    for title in found_titles:
        for batch in items[title]:
            total += batch["amount"]
    return total


# --- Тестирование ---
if __name__ == "__main__":
    add(goods, "яблоки", 10, "2025-12-01")
    add(goods, "яблоки", 5, "2025-12-10")
    add(goods, "молоко", 2.5, "2024-06-15")

    print("После ручного добавления:", goods)

    add_by_note(goods, "мороженое ванильное 1.5 2025-07-01")
    add_by_note(goods, "арбуз большой 5 2024-08-10")

    print("\nПосле добавления по заметкам:", goods)

    print("\nПоиск 'яблоки':", find(goods, "яблоки"))
    print("Поиск 'око':", find(goods, "око"))
    print("Поиск 'большой':", find(goods, "большой"))

    print("\nКоличество продуктов с 'яблоки':", amount(goods, "яблоки"))
    print("Количество продуктов с 'око':", amount(goods, "око"))
    print("Количество продуктов с 'о':", amount(goods, "о"))

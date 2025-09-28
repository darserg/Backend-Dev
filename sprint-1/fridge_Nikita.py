from datetime import datetime
from decimal import Decimal, getcontext

getcontext().prec = 4
DATE_FORMAT = "%Y-%m-%d"
goods = {}


def add(*args):
    title, amount, expiration_date = args[:3]
    exp_date = datetime.strptime(expiration_date, DATE_FORMAT)
    if title not in goods:
        goods[title] = []
    goods[title].append({"amount": Decimal(str(amount)), "expiration_date": exp_date})


def add_by_note(note):
    parts = note.split()
    if len(parts) >= 3 and "-" in parts[-1]:
        expiration_date = parts[-1]
        amount_str = parts[-2]
        product_name_parts = parts[:-2]
        title = " ".join(product_name_parts)
        amount = Decimal(amount_str)
        add(title, amount, expiration_date)
    else:
        print("Неверный формат записи. Ожидается: 'Название количество дата'")


def find(query):
    found = []
    query_lower = query.lower()
    for title in goods.keys():
        if query_lower in title.lower():
            found.append(title)
    return found


def amount(query):
    total = Decimal("0")
    found_products = find(query)
    for title in found_products:
        for batch in goods[title]:
            total += batch["amount"]
    return total


add("Молоко", 1, "2025-06-30")
add("Яйца", 10, "2025-07-15")
add_by_note("Молоко 1 2025-06-30")
add_by_note("Куриные яйца 10 2025-07-15")

print("Все продукты:", goods)
print("Найдено по 'мол':", find("мол"))
print("Общее количество по 'мол':", amount("мол"))
print("Найдено по 'яй':", find("яй"))
print("Общее количество по 'яй':", amount("яй"))

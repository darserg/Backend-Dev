def pay_bills(month, bills):
    # Ваш код здесь
    if month % 3 == 0:
        return bills[1 : len(bills) - 1]
    else:
        return [bills[0], bills[-1]]


# Вызов функции:
print(pay_bills(5, ["Интернет", "Коммуналка", "Телефон", "Страховка"]))

from decimal import Decimal, getcontext

getcontext().prec = 3


def get_monthly_payment(total_sum, months_count, percents):
    monthly_raw = Decimal(total_sum) / Decimal(str(months_count))
    monthly_addition = monthly_raw * Decimal(str(percents / 100))
    total = monthly_addition + monthly_raw
    return total


payment_value = get_monthly_payment(54, 24, 9)
print("Ежемесячный платёж:", payment_value, "ВтК")

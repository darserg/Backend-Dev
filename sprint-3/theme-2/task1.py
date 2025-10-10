class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name_value, amount_value):
        self.name = name_value
        self.amount = amount_value

    def get_info(self):
        return f"{self.name} (в наличии: {self.amount})"


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, name_value, amount_value, weight_value):
        super().__init__(name_value, amount_value)
        self.weight = weight_value

    def get_weight(self):
        return f"{self.name} (в наличии: {self.amount}). Вес: {self.weight} кг"


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, name_value, amount_value, size_value):
        super().__init__(name_value, amount_value)
        self.size = size_value

    def get_size(self):
        return f"{self.name} (в наличии: {self.amount}). Размер: {self.size}"


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell("Гиря малая", 15, 2)
shirt = Clothing("Футболка", 5, "L")

print(small_kettlebell.get_weight())
print(shirt.get_size())

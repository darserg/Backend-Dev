from typing import Optional


class User:
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError("Необходимо указать параметры пользователя")

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Метод класса with_name — альтернативный конструктор по имени и фамилии
    @classmethod
    def with_name(cls, first_name: str, last_name: str):
        return cls(first_name=first_name, last_name=last_name)

    # Метод класса with_username — альтернативный конструктор по псевдониму
    @classmethod
    def with_username(cls, username: str):
        if not cls.is_username_allowed(username):
            raise ValueError("Некорректное имя пользователя")
        return cls(username=username)

    # Статический метод для проверки корректности username
    @staticmethod
    def is_username_allowed(username: str) -> bool:
        return not username.startswith("admin")

    # Свойство full_name — возвращает полное имя или @username
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return f"@{self.username}"
        else:
            return (
                ""  # на случай, если не задано ничего (хотя по условию это невозможно)
            )


stas = User.with_name("Стас", "Басов")
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
try:
    ne_stas = User.with_username("admin_nestas_anonymous")
except ValueError as e:
    print(f"Ошибка: {e}")

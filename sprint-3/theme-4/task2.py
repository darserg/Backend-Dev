def obfuscator(func):
    def wrapper():
        credentials = func()
        # Обрабатываем имя: оставляем первый и последний символ, остальное — звёздочки
        if "name" in credentials and isinstance(credentials["name"], str):
            name = credentials["name"]
            if len(name) <= 2:
                credentials["name"] = name  # если имя короткое — не меняем
            else:
                credentials["name"] = name[0] + "*" * (len(name) - 2) + name[-1]

        # Обрабатываем пароль: все символы заменяем на звёздочки
        if "password" in credentials and isinstance(credentials["password"], str):
            credentials["password"] = "*" * len(credentials["password"])

        return credentials

    return wrapper


@obfuscator
def get_credentials():
    return {"name": "StasBasov", "password": "iamthebest"}


print(get_credentials())

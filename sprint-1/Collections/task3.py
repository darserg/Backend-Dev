def is_palindrome(string):
    # Ваш код здесь
    string = string.replace(" ", "").lower()
    return string == string[::-1]


# Должно быть напечатано True:
print(is_palindrome("А роза упала на лапу Азора"))
# Должно быть напечатано False:
print(is_palindrome("Не палиндром"))

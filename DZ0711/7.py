def is_palindrome(number):
    # Преобразуем число в строку
    str_number = str(number)
    # Сравниваем строку с её обратной версией
    return str_number == str_number[::-1]

# Примеры использования функции
print(is_palindrome(123321))  # True
print(is_palindrome(546645))  # True
print(is_palindrome(421987))  # False

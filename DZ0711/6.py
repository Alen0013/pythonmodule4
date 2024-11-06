def count_digits(number):
    # Преобразуем число в строку и считаем длину строки
    return len(str(abs(number)))  # Используем abs для обработки отрицательных чисел

# Пример использования функции
digit_count = count_digits(3456)
print("Количество цифр в числе:", digit_count)

digit_count_negative = count_digits(-12345)
print("Количество цифр в числе:", digit_count_negative)

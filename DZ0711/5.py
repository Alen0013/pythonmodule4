def product_in_range(start, end):
    # Меняем местами границы, если это необходимо
    lower = min(start, end)
    upper = max(start, end)

    product = 1
    for num in range(lower, upper + 1):
        product *= num

    return product


# Пример использования функции
result = product_in_range(5, 3)
print("Произведение чисел в диапазоне:", result)

result = product_in_range(2, 4)
print("Произведение чисел в диапазоне:", result)

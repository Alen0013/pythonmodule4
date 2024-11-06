def display_even_numbers(start, end):
    lower = min(start, end)
    upper = max(start, end)

    even_numbers = [num for num in range(lower, upper + 1) if num % 2 == 0]

    print("Четные числа между", lower, "и", upper, ":", even_numbers)

display_even_numbers(10, 20)  

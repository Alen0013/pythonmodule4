def display_square(size, symbol, filled):
    if filled:
       
        for _ in range(size):
            print(symbol * size)
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + ' ' * (size - 2) + symbol)

print("Заполненный квадрат:")
display_square(5, '*', True)

print("\nПустой квадрат:")
display_square(5, '*', False)

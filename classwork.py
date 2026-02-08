side = int(input('Введіть довжину сторони: '))
symbol = input('Введіть символ: ')

for i in range(1, side // 2 + 1):
    for j in range(1, side // 2 + 1):
        if j < i:
            print(symbol, end='')
        else:
            print(' ', end='')

    for j in range(side // 2, 0, -1):
        if j < i:
            print(symbol, end='')
        else:
            print(' ', end='')
    print()

for i in range(1, side // 2 + 1):
    for j in range(side // 2, 0, -1):
        if j < i:
            print(' ', end='')
        else:
            print(symbol, end='')

    for j in range(1, side // 2 + 1):
        if j < i:
            print(' ', end='')
        else:
            print(symbol, end='')
    print()
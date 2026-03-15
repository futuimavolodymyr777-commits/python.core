try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    action = input('Enter operation(+, -, *, /): ')

    match action:
        case '+': print(f'{num1} + {num2} = {num1 + num2}')
        case '-': print(f'{num1} - {num2} = {num1 - num2}')
        case '*': print(f'{num1} * {num2} = {num1 * num2}')
        case '/': print(f'{num1} / {num2} = {num1 / num2}')
except:
    print('Incorrect number!')
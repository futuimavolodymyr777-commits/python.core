operators = ['+', '-', '*', '/']

while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        action = input('Enter operation(+, -, *, /): ')

        if action not in operators:
            raise Exception(action)

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ValueError:
        print('Incorrect number!')
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except Exception as ex:
        print(f'Incorrect operation! {ex.args[0]}')
    finally:
        reapeat = input('Do you want to repeat? Y/N ')
        if reapeat.lower() == 'n':
            break
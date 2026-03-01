def print_full_name(last_name, first_name):
    print("Повне ім'я:", last_name, first_name)


print_full_name('Ковальчук', 'Антон')
print_full_name(last_name='Ковальчук', first_name='Антон')

def my_animal(type, name, age):
    print(f'У мене є {type} на ім\'я {name}. Вік: {age}')


my_animal('собака', age=10, name='Патрон')
def my_sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(my_sum(10,12, 34))
print(my_sum(10))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10))
def unpack_positional(a, b, c):
    print(a, b, c, sep=', ')


fruits = ['apple', 'orange', 'banana']
unpack_positional(*fruits)


def unpack_kw_args(red, green, yellow):
    print(red, green, yellow)


fruits = {
    'red': 'apple',
    'green': 'pear',
    'yellow': 'banana'
}

unpack_kw_args(**fruits)
# юзер вводит числа через пробел
numbers_input = input("введи числа через пробел: ").split()

numbers = []
# пробегаемся по введённым значениям
# и руками превращаем строки в числа
for n in numbers_input:
    numbers.append(int(n))

# sum() сама складывает все элементы списка
total = sum(numbers)

average = total / len(numbers) if numbers else 0

print("сумма всех элементов:", total)
print("среднее арифметическое:", average)


target = int(input("введи число которое ищем: "))

count = numbers.count(target)

print("сколько раз встречается число:", count)


# тут sum() + генератор
# он перебирает список и берет только положительные
positive_sum = sum(num for num in numbers if num > 0)

print("сумма положительных чисел:", positive_sum)


even_indices = [i for i, num in enumerate(numbers) if num % 2 == 0]

print("индексы четных чисел:", even_indices)


unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("уникальные элементы без повторов:", unique_numbers)

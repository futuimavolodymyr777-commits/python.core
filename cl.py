#юзер вводит список чисел
numbers = list(map(int, input("введи числа через пробел: ").split()))

#считаем сумму
total = sum(numbers)

#считаем среднее арифметическое
average = total / len(numbers) if numbers else 0

print("сумма всех элементов:", total)
print("среднее арифметическое:", average)

#юзер вводит число которое нужно найти
target = int(input("введи число которое ищем: "))

#считаем сколько раз оно встречается
count = numbers.count(target)

print("сколько раз встречается число:", count)

#считаем сумму положительных чисел
positive_sum = sum(num for num in numbers if num > 0)

print("сумма положительных чисел:", positive_sum)

#ищем индексы всех четных чисел
even_indices = [i for i, num in enumerate(numbers) if num % 2 == 0]

print("индексы четных чисел:", even_indices)

#оставляем только уникальные элементы без повторов
unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("уникальные элементы без повторов:", unique_numbers)
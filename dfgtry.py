import random

#задание 1
#считаем степень через рекурсию

def power(number, degree):
    #если степень 0 → всегда 1
    if degree == 0:
        return 1
    
    #умножаем число и уменьшаем степень
    return number * power(number, degree - 1)

print("степень:", power(2,5))


#задание 2
#чек високосный год или нет

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


#переводим дату в общее количество дней
#типа считаем сколько дней прошло

def date_to_days(day, month, year):

    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    total_days = day

    #накидываем дни за прошлые года
    for current_year in range(1, year):
        if is_leap_year(current_year):
            total_days += 366
        else:
            total_days += 365

    #накидываем дни за месяцы
    for current_month in range(month-1):
        total_days += month_days[current_month]

    #если после февраля и год високосный
    if month > 2 and is_leap_year(year):
        total_days += 1

    return total_days


#считаем разницу между двумя датами
def days_difference(day1, month1, year1, day2, month2, year2):
    return abs(date_to_days(day1,month1,year1) - date_to_days(day2,month2,year2))

print("разница дней:", days_difference(1,1,2024,10,1,2024))


#задание 3
#генерим список из 100 случайных чисел

numbers = [random.randint(-100,100) for i in range(100)]


#рекурсивно ищем где начинается кусок из 10 чисел
#у которого самая маленькая сумма

def find_min_sum_position(numbers_list, index=0, min_sum=None, min_position=0):

    #если уже конец списка
    if index > len(numbers_list) - 10:
        return min_position

    #сумма текущих 10 чисел
    current_sum = sum(numbers_list[index:index+10])

    #если нашли меньше
    if min_sum is None or current_sum < min_sum:
        min_sum = current_sum
        min_position = index

    #идем дальше
    return find_min_sum_position(numbers_list, index+1, min_sum, min_position)


position = find_min_sum_position(numbers)

print("позиция:", position)
print("10 чисел:", numbers[position:position+10])
print("сумма:", sum(numbers[position:position+10]))

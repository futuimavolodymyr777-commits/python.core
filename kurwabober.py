#задание 1
def task1():
    # тупо выводим цитатку без заморочек
    print('"Don\'t let the noise of others\' opinions')
    print('drown out your own inner voice."')
    print('Steve Jobs')


#задание 2
def task2(a, b):
    # если чел накосячил и ввел наоборот фиксим
    if a > b:
        a, b = b, a
    
    # бегаем по числам между ними
    for i in range(a + 1, b):
        # если не делится на 2 значит норм нечетное
        if i % 2 != 0:
            print(i)


# адание 3
def task3(dlina, napr, simvol):
    # если надо в строку просто спамим символ
    if napr == "h":
        print(simvol * dlina)
    # иначе долбим в столбик
    else:
        for i in range(dlina):
            print(simvol)


#задание 4
def task4(a, b, c, d):
    # просто берем самое жирное число
    return max(a, b, c, d)


#задание 5
def task5(n):
    # все что меньше 2 сразу мимо
    if n < 2:
        return False
    
    # чекаем делится ли хоть на что то
    for i in range(2, n):
        if n % i == 0:
            return False
    
    # если ни на что не делится значит число топ простое
    return True


#задание 6
def task6(n):
    # превращаем число в текст чтоб ковырять цифры
    s = str(n)
    
    # если цифр не шесть это вообще не тот движ
    if len(s) != 6:
        return False
    
    # считаем левую сторону
    sum1 = int(s[0]) + int(s[1]) + int(s[2])
    
    # считаем правую сторону
    sum2 = int(s[3]) + int(s[4]) + int(s[5])
    
    # если совпало значит билетик фартовый
    return sum1 == sum2
import random

#задание 1
#рекурсия чтобы посчитать степень

def power(a, n):
    #если степень 0 то ответ 1
    if n == 0:
        return 1
    #иначе просто умножаем и уменьшаем степень
    return a * power(a, n-1)

print(power(2,5))  # чек


#задание 2
#чек високосный год или нет

def leap(y):
    return (y%4==0 and y%100!=0) or y%400==0


#переводим дату в дни (чтобы потом вычесть)
def days(d,m,y):

    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=d

    #накидываем дни за прошлые года
    for i in range(1,y):
        total+=366 if leap(i) else 365

    #накидываем дни за месяцы
    for i in range(m-1):
        total+=months[i]

    #если после февраля в високосный год
    if m>2 and leap(y):
        total+=1

    return total


#разница между датами
def diff(d1,m1,y1,d2,m2,y2):
    return abs(days(d1,m1,y1)-days(d2,m2,y2))

print(diff(1,1,2024,10,1,2024))  # чек


#задание 3
#генерим 100 рандомных чисел

nums=[random.randint(-100,100) for _ in range(100)]


#рекурсивно ищем где 10 чисел дают мин сумму
def find_min(a,i=0,best=None,pos=0):

    #если почти конец списка
    if i>len(a)-10:
        return pos

    s=sum(a[i:i+10])  # сумма 10 чисел

    #если нашли меньше
    if best is None or s<best:
        best=s
        pos=i

    #идём дальше
    return find_min(a,i+1,best,pos)


p=find_min(nums)

print("позиция:",p)
print("сумма:",sum(nums[p:p+10]))
import turtle as t
import random

#функция для 1 зад
def task_1():
    t.clear()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    
    #ред квадрат
    t.color("red")
    for i in range(4):
        t.forward(50)
        t.right(90)
    
    #в сторону
    t.penup()
    t.forward(100)
    t.pendown()
    
    #зеленый треугольнитк
    t.color("green")
    for i in range(3):
        t.forward(60)
        t.left(120)
        
    #еще дальше
    t.penup()
    t.forward(120)
    t.pendown()
    
    #синий пятиугольник
    t.color("blue")
    for i in range(5):
        t.forward(50)
        t.right(72)

#функция для 2 зад
def task_2():
    t.clear()
    #стены дома
    t.color("black", "grey")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    #переход к крыше
    t.penup()
    t.goto(0, 100)
    t.pendown()
    
    #крыша
    t.color("black", "red")
    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.end_fill()

#функция для 3 зад
def task_3():
    t.clear()
    t.speed(0)
    t.colormode(255)
    #цикл для 36 квадратов
    for i in range(36):
        #выбираем случайный цвет
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        t.pencolor(r, g, b)
        
        #один квадрат
        for j in range(4):
            t.forward(100)
            t.right(90)
        #поворачиваем сетку
        t.right(10)

#меню
print("выбери номер задания:")
print("1 - три фигуры")
print("2 - домик")
print("3 - узор из квадратов")

choice = input("твой выбор: ")

if choice == "1":
    task_1()
elif choice == "2":
    task_2()
elif choice == "3":
    task_3()

t.done()
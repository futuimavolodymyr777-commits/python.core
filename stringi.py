def figure_e():
    #крест
    for i in range(5):
        for j in range(5):
            if i == j or i + j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_zh():
    #треугольник вправо
    for i in range(5):
        for j in range(5):
            if j >= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_z():
    #треугольник влево
    for i in range(5):
        for j in range(5):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_i():
    #диагональ снизу вверх
    for i in range(5):
        for j in range(5):
            if j >= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_k():
    #диагональ сверху-вниз
    for i in range(5):
        for j in range(5):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_a():
    #диагональ снизу влево
    for i in range(5):
        for j in range(5):
            if j >= i:
                print(" ", end="")
            else:
                print("*", end="")
        print()

def figure_b():
    #диагональ снизу вправо
    for i in range(5):
        for j in range(5):
            if j <= i:
                print(" ", end="")
            else:
                print("*", end="")
        print()

def figure_v():
    #треугольник вниз
    for i in range(5):
        for j in range(5):
            if j >= i and j <= 4 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_g():
    #треугольник вверх
    for i in range(5):
        for j in range(5):
            if j <= i and j >= 4 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def figure_d():
    #крест
    for i in range(5):
        for j in range(5):
            if i == j or i + j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# ловарь фигур
figures = {
    "е": figure_e,
    "ж": figure_zh,
    "з": figure_z,
    "и": figure_i,
    "к": figure_k,
    "а": figure_a,
    "б": figure_b,
    "в": figure_v,
    "г": figure_g,
    "д": figure_d
}

# меню
print("доступные фигуры: е, ж, з, и, к, а, б, в, г, д")
choice = input("выберите фигуру: ")

if choice in figures:
    figures[choice]()
else:
    print("такой фигуры нет")
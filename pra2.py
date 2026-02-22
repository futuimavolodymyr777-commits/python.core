import random  # рандомчик

# уникальные числа
nums = input("накидай числа: ").split()
print("уникальные:", set(nums))  # выкинули повторы

# два рандомных набора
s1 = {random.randint(1,20) for _ in range(10)}
s2 = {random.randint(1,20) for _ in range(10)}
print("первый:", s1)
print("второй:", s2)
print("общие:", s1 & s2)      # пересечение
print("разница:", s1 - s2)    # что только в первом
print("всё вместе:", s1 | s2) # объединение

# анаграммы
w1 = input("слово1: ").lower()
w2 = input("слово2: ").lower()
if set(w1)==set(w2):
    print("анаграммы ")
else:
    print("не анаграммы ")
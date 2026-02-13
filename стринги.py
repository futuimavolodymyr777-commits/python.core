# меню
print("1 - подсчет предложений")
print("2 - проверка на палиндром")
print("3 - зарезервированные слова в верхний регистр")
print("4 - удаление символов между двумя символами")
print("5 - удаление слов с заданными символами")
print("6 - переворот слов")

choice = input("выберите номер задания: ")

#задание 1
if choice == "1":
    text = input("введите текст: ")
    # считаем точки восклицателные и вопросительные знаки
    count = text.count(".") + text.count("!") + text.count("?")
    print("количество предложений:", count)

#задание 2
elif choice == "2":
    text = input("введите строку: ")
    # убираем пробелы и делаем маленькие буквы
    text = text.replace(" ", "").lower()
    # сравниваем строку с перевкрнутой
    if text == text[::-1]:
        print("это палиндром")
    else:
        print("это не палиндром")

#задание 3
elif choice == "3":
    reserved = ["if", "else", "for", "while", "return"]
    text = input("введите текст: ")
    words = text.split()

    for i in range(len(words)):
        if words[i].lower() in reserved:
            words[i] = words[i].upper()

    print("измененный текст:")
    print(" ".join(words))

#задание 4
elif choice == "4":
    text = input("введите строку: ")
    a = input("введите первый символ: ")
    b = input("введите второй символ: ")

    start = text.find(a)
    end = text.find(b)

    # если оба символа найдены
    if start != -1 and end != -1 and start < end:
        text = text[:start] + text[end+1:]

    print("результат:", text)

#задание 5
elif choice == "5":
    text = input("введите текст: ")
    symbols = input("введите набор символов: ")

    words = text.split()
    result = []

    for word in words:
        delete = False
        for s in symbols:
            if s in word:
                delete = True
        if not delete:
            result.append(word)

    print("результат:")
    print(" ".join(result))

#задание 6
elif choice == "6":
    text = input("введите текст: ")
    words = text.split()
    words.reverse()  # переворачиваем спмсок слов
    print("обратный текст:")
    print(" ".join(words))

else:
    print("неверный выбор")
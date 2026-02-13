print("1 - предложения")
print("2 - палиндром")
print("3 - зарезервированные слова")
print("4 - удалить между символами")
print("5 - удалить слова с символами")
print("6 - переворот слов")

n = input("номер задания: ")

#1 считаем конец предложений
if n == "1":
    text = input("введите текст: ")
    count = 0
    for c in text:
        if c == "." or c == "!" or c == "?":
            count = count + 1
    print("количество предложений:", count)

#2 палиндром.
elif n == "2":
    text = input("введите строку: ")
    text = text.replace(" ", "").lower()

    rev = ""
    i = len(text) - 1
    while i >= 0:
        rev = rev + text[i]
        i = i - 1

    if text == rev:
        print("палиндром")
    else:
        print("не палиндром")

#3 делаем нужные слова большими ЖИРНЫМИ ТОХА Т2Х2
elif n == "3":
    text = input("введите текст: ")
    words = text.split()

    for word in words:
        if word == "if" or word == "else" or word == "for" or word == "while" or word == "return":
            print(word.upper(), end=" ")
        else:
            print(word, end=" ")

#4 вырезаем кусок между символами
elif n == "4":
    text = input("введите строку: ")
    a = input("первый символ: ")
    b = input("второй символ: ")

    start = text.find(a)
    end = text.find(b)

    if start != -1 and end != -1 and start < end:
        i = 0
        while i < len(text):
            if i < start or i > end:
                print(text[i], end="")
            i = i + 1
    else:
        print(text)

#5 убираем слова с лишними кило... ой символами
elif n == "5":
    text = input("введите текст: ")
    symbols = input("введите символы: ")

    words = text.split()

    for word in words:
        delete = False
        for s in symbols:
            if s in word:
                delete = True
        if delete == False:
            print(word, end=" ")

#6 выводим слова наоборот
elif n == "6":
    text = input("введите текст: ")
    words = text.split()

    i = len(words) - 1
    while i >= 0:
        print(words[i], end=" ")
        i = i - 1

else:
    print("неверный номер")

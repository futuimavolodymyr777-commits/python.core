#задание1 считаем количество букв и цифр в строке

text = input("введите строку: ")

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("количество букв:", letters)
print("количество цифр:", digits)

print("-" * 30)

#задение2 считаем сколько раз символ встречается в строке

text = input("введите строку: ")
symbol = input("введите символ для поиска: ")

count = 0

for ch in text:
    if ch == symbol:
        count += 1

print("символ встречается", count, "раз")

print("-" * 30)

#задание3 переворачиваем строку без использования срезов

text = input("введите строку: ")

reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("перевернутая строка:", reversed_text)

print("-" * 30)

#задание4 считаем сколько раз слово встречается в строке

text = input("введите строку: ")
search_word = input("введите слово для поиска: ")

words = text.split()
count = 0

for word in words:
    if word == search_word:
        count += 1

print("слово встречается", count, "раз")

print("-" * 30)

#запание5 заменяем одно слово на другое в строке

text = input("введите строку: ")
old_word = input("введите слово для поиска: ")
new_word = input("введите слово для замены: ")

result = text.replace(old_word, new_word)

print("результат:", result)

print("-" * 30)

#задание6 находим самое длинное слово в строке

text = input("введите строку: ")

words = text.split()
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("самое длинное слово:", longest_word)
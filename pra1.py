# наш мини телефончик
contacts = {}

while True:
    print("\n1 - добавить")
    print("2 - удалить")
    print("3 - показать")
    print("0 - выход")

    choice = input("че жмем: ")

    if choice == "1":
        name = input("имя: ")
        phone = input("телефон: ")
        contacts[name] = phone  # закинули чела в список

    elif choice == "2":
        name = input("имя: ")
        if name in contacts:
            del contacts[name]  # убрали чела, минус один

    elif choice == "3":
        for name in contacts:
            print(name, ":", contacts[name])  # палим весь движ

    elif choice == "0":
        break  # все, погнали отсюда


# ща считаем слова, кто сколько раз засветился
text = input("\nнакидай текст: ").lower().split()
word_count = {}

for word in text:
    word_count[word] = word_count.get(word, 0) + 1  # плюсик слову

for word in word_count:
    print(word, ":", word_count[word])  # смотрим статистику


# мини обменник, типа считаем бабки
rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("\nкакая валюта (usd, eur, pln): ").upper()
amount = float(input("сколько грн: "))

if currency in rates:
    result = amount / rates[currency]
    print("получится:", round(result, 2), currency)  # математика произошла


# переводчик на минималках
dictionary = {
    "cat": "кот",
    "dog": "собака",
    "car": "машина"
}

word = input("\nче переводим: ").lower()

if word in dictionary:
    print("это будет:", dictionary[word])  # нашли перевод, кайф
else:
    print("такого слова нет, сорян")  # ну бывает
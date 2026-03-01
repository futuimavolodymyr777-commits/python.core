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
        # тут мы используем словарь: ключ=name, значение=phone
        # если такой ключ уже есть, значение перезапишется автоматически

    elif choice == "2":
        name = input("имя: ")
        if name in contacts:
            del contacts[name]  # убрали чела, минус один
            # ключ удаляется полностью, и его значение тоже пропадает
        # если ключа нет, ошибка не выдается, потому что проверили через if

    elif choice == "3":
        for name in contacts:
            print(name, ":", contacts[name])  # палим весь движ
            # перебираем словарь по ключам
            # contacts[name] достаем значение по ключу
            # это важно: словари не индексируются по числу, а по ключу

    elif choice == "0":
        break  # все, погнали отсюда


# ща считаем слова, кто сколько раз засветился
text = input("\nнакидай текст: ").lower().split()
word_count = {}

for word in text:
    word_count[word] = word_count.get(word, 0) + 1  # плюсик слову
    # .get(key, default) возвращает значение ключа, если ключа нет - возвращает default
    # таким образом не возникает ошибки KeyError при первом появлении слова

for word in word_count:
    print(word, ":", word_count[word])  # смотрим статистику
    # перебор словаря по ключам, можно было использовать .items() чтобы сразу получить ключ и значение


# мини обменник, типа считаем бабки
rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("\nкакая валюта (usd, eur, pln): ").upper()
amount = float(input("сколько грн: "))

if currency in rates:
    result = amount / rates[currency]
    print("получится:", round(result, 2), currency)  # математика произошла
    # словарь rates хранит "валюта": курс
    # проверка "if currency in rates" ищет ключ словаря
    # round округляет число до 2 знаков после запятой


# переводчик на минималках
dictionary = {
    "cat": "кот",
    "dog": "собака",
    "car": "машина"
}

word = input("\nче переводим: ").lower()

if word in dictionary:
    print("это будет:", dictionary[word])  # нашли перевод, кайф
    # словарь используется для быстрого поиска соответствия ключ -> значение
else:
    print("такого слова нет, сорян")  # ну бывает
    # здесь мы не создаем ошибку KeyError, потому что проверили наличие ключа

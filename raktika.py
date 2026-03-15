#главное меню
while True:
    print("\nвыбери задание 1-6 или 0 для выхода") #меню
    choice = input("номер задания: ")

    #задание1 финальная цена
    if choice == "1":
        try:
            p = float(input("цена: ")) #юзер вводит цену
            d = float(input("скидка %: ")) #юзер вводит скидку
            print("финальная цена", p*(1-d/100)) #бах и финальная цена
        except:
            print("йо введи число") #если не число

    #задание2 доллары в евро
    if choice == "2":
        try:
            usd = float(input("доллары: ")) #сколько баксов
            rate = float(input("курс: ")) #курс евро
            if rate == 0: print("курс 0 нельзя") #проверка
            else: print("евро на руках", usd*rate) #показываем бабло
        except:
            print("введи число")
        print("операция готова") #конец блока

    #задание3 средняя оценка
    if choice == "3":
        try:
            s = input("оценки через пробел: ") #юзер вводит баллы
            l = []
            for x in s.split():
                if x.isdigit(): l.append(int(x)) #норм числа
                else: print("фигня пропущена", x) #предупреждение
            if len(l) > 0: print("средняя", sum(l)/len(l)) #среднее
            else: print("нет норм чисел")
        except:
            print("ошибка")
        print("готово")

    #задание4 банкомат
    if choice == "4":
        b = 1000 #баланс
        try:
            a = int(input("снять: "))
            if a % 10 != 0 or a > b: print("неправильная сумма") #проверка
            else: print("снял", a)
        except:
            print("ошибка")
        print("транзакция готова")

    #задание5 проверка номера заказа
    if choice == "5":
        o = input("номер заказа: ")
        if o[:3]!="ORD": print("надо с ORD") #роверка начала
        elif not o[3:].isdigit(): print("после ORD цифры") #проверка цифр
        else: print("номер ок")
        print("проверка готова")

    #заданиие6 сумма и среднее
    if choice == "6":
        s = input("числа через пробел: ")
        nums = []
        for x in s.split():
            if x.replace(".","",1).isdigit(): nums.append(float(x)) # число норм
            else: print("фигня пропущена", x) #предупреждаем
        if len(nums) > 0:
            total = sum(nums)
            avg = total / len(nums)
            print("сумма", total, "среднее", avg) #показываем
        else:
            print("нет норм чисел")
        print("готово")

    #выход
    if choice == "0":
        print("выход из проги") #юзер ушёл
        break

    #неверный ввод
    if choice not in ["0","1","2","3","4","5","6"]:
        print("неверный номер") #юзер ввёл фигню иди учи уроки
file_path = "data.txt"  #файл с данными наш исходник
music_file = "music_collection.txt"  #тут музончик хранится

while True:
    #главное меню, чо делать
    print("\n1 - копия файла")
    print("2 - зашифровать файл")
    print("3 - музон")
    print("4 - выход")

    choice = input("выбирай: ")

    #копируем файл (бэкапчик делаем)
    if choice == "1":
        with open(file_path, 'r') as file:
            text = file.read()  #читаем всё подряд

        with open("backup.txt", 'w') as file:
            file.write(text)  #в новый файл скидываем

        print("готово, скопировал")

    #шифруем каждую букву двигаем вперёд
    elif choice == "2":
        with open(file_path, 'r') as file:
            text = file.read()  #читаем исходник

        result = ""  #сюда будем собирать новый текст

        for char in text:
            if char.isalpha():  #если буква
                if char == 'z':
                    result += 'a'  #z → a
                elif char == 'Z':
                    result += 'A'  #Z → A
                else:
                    result += chr(ord(char) + 1)  #обычный сдвиг
            else:
                result += char  #всё остальное оставляем

        with open("encrypted.txt", 'w') as file:
            file.write(result)  #в файл скидываем

        print("готово, шифр на месте")

    #меню с музоном
    elif choice == "3":
        while True:
            print("\n музон меню")
            print("1 добавить")
            print("2 показать")
            print("3 поиск")
            print("4 удалить")
            print("5 назад")

            m_choice = input("выбор: ")

            #докинуть альбом
            if m_choice == "1":
                title = input("название альбома: ")
                artist = input("исполнитель: ")
                year = input("год: ")

                with open(music_file, 'a') as file:
                    file.write(title + "|" + artist + "|" + year + "\n")  #пушим в конец

            #показать всю коллекцию
            elif m_choice == "2":
                with open(music_file, 'r') as file:
                    for line in file:
                        print(line.strip())  #убираем лишние \n

            #поиск по исполнителю
            elif m_choice == "3":
                name = input("кого ищем: ")
                with open(music_file, 'r') as file:
                    for line in file:
                        if name.lower() in line.lower():  #ищем без учёта регистра
                            print(line.strip())

            #удалить альбом
            elif m_choice == "4":
                delete_name = input("что удаляем: ")

                with open(music_file, 'r') as file:
                    lines = file.readlines()  #читаем всё

                with open(music_file, 'w') as file:
                    for line in lines:
                        if delete_name.lower() not in line.lower():  #фильтруем
                            file.write(line)

            #назад в главное меню
            elif m_choice == "5":
                break

            else:
                print("чё-то не то нажал")

    #выход из программы
    elif choice == "4":
        print("выходим, пока")
        break

    else:
        print("не понял, повтори")
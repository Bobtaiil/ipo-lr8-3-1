#Импортируем библиотеку json 
import json

#Имя файла
file = 'stars.json'

#Создаём список с данными о звёздах
data_about_stars_1 = [
    {"id": 1, "name": "Сириус", "constellation": "Большой Пес", "is_visible": True, "radius": 1.71},
    {"id": 2, "name": "Канопус", "constellation": "Корма", "is_visible": True, "radius": 0.73},
    {"id": 3, "name": "Арктур", "constellation": "Богатырь", "is_visible": True, "radius": 1.5},
    {"id": 4, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.13},
    {"id": 5, "name": "Полиус", "constellation": "Центавр", "is_visible": False, "radius": 1.3}
]
#Открываем json файл
with open(file, 'w') as f:
    json.dump(data_about_stars_1, f) 

#Создаём переменную кол-ва операций
count_of_operations = 0

#Отображение звёзд
def display_all_stars():
    #Открываем файл и загружаем данные
    with open(file, 'r') as f:
        stars = json.load(f)
        print("\nВсе записи:")
        #Перебор объектов и запись в json
        for star in stars:
            print(json.dumps(star, ensure_ascii = False, indent = 4))

#Поиск по ID
def find_star_by_id(ID):
    #Открываем файл и загружаем данные
    with open(file, 'r') as f:
        stars = json.load(f)
        #Поиск по ID
        for index, star in enumerate(stars):
            #Если star[id] = ID или не равен
            if star['id'] == ID:
                print(f"\nЗапись найдена (позиция {index + 1}):")
                print(json.dumps(star, ensure_ascii = False, indent = 4))
                return True
        print("Запись не найдена.")
        return False

#Добавление звезды
def add_star():
    #Словарь для звезды
    new_star = {}
    
    while True:
        try:
            #Ввод с проверкой
            new_star['id'] = int(input("Введите ID записи: "))
            break
        except ValueError:
            print("неверный ID")
    
    #Ввод данных с проверками
    new_star['name'] = input("Введите название звезды: ")
    new_star['constellation'] = input("Введите название созвездия: ")
    
    while True:
        is_visible_input = input("Можно ли увидеть звезду без телескопа (True/False): ")
        if is_visible_input in ['True', 'False']:
            new_star['is_visible'] = is_visible_input == 'True'
            break
        else:
            print("Введите true / false.")
    
    while True:
        try:
            new_star['radius'] = float(input("Введите солнечный радиус звезды: "))
            break
        except ValueError:
            print("Некорректный радиус.")
    
    #Открываем файл и загружаем данные + проверки
    with open(file, 'r') as f:
        stars = json.load(f)
    
    if any(star['id'] == new_star['id'] for star in stars):
        print("Запись с этим ID уже существует.")
        return
    
    #Добавляем звезду в список
    stars.append(new_star)

    #Открываем файл и сохраняем список
    with open(file, 'w') as f:
        json.dump(stars, f)

    print("Запись добавлена.")

#Удаление звезды по ID
def remove_star(ID_remove):
    #Открываем файл и сохраняем данные
    with open(file, 'r') as f:
        stars = json.load(f)
    
    #отслеживание успешного выполнения поиска
    found = False
    #поиск по ID с проверками и соотв. действиями
    for index, star in enumerate(stars):
        if star['id'] == ID_remove:
            del stars[index]
            found = True
            break

    if found:
        #Открываем файл и сохраняем список + проверки
        with open(file, 'w') as f:
            json.dump(stars, f)
        print("Запись удалена.")
    else:
        print("Запись не найдена.")

#Цикл, работающий до выхода из программы
while True:
    #Меню
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")

    #выбор опции
    user_choice = input("Выберите пункт меню: ")

    #Если 1
    if user_choice == '1':
        #Отображение списка звёзд
        display_all_stars()
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если 2
    elif user_choice == '2':
        while True:
            try:
                #Ввод ID и поиск по ID + проверка
                ID = int(input("Введите ID записи для поиска: "))
                find_star_by_id(ID)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                print("Пожалуйста, введите корректный числовой ID.")

    #Если 3
    elif user_choice == '3':
        #Добавление звезды
        add_star()
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если 4
    elif user_choice == '4':
        while True:
            try:
                #Ввод Id для удаления + проверка
                ID_remove = int(input("Введите ID записи для удаления: "))
                remove_star(ID_remove)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                print("Пожалуйста, введите корректный числовой ID.")

    #Если 5
    elif user_choice == '5':
        #Вывод
        print(f"Количество выполненных операций: {count_of_operations}")
        #Выход
        break  
    else:
        print("Необходимо ввести от 1 до 5 пункта")
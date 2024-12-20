#Импортируем библиотеку json 
import json

#имя файла
file = 'stars.json'

#Создаём список с данными о звёздах
data_about_stars_1 = [
    {"id": 1, "name": "Сириус", "constellation": "Большой Пес", "is_visible": True, "radius": 1.71},
    {"id": 2, "name": "Канопус", "constellation": "Корма", "is_visible": True, "radius": 0.73},
    {"id": 3, "name": "Арктур", "constellation": "Богатырь", "is_visible": True, "radius": 1.5},
    {"id": 4, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.13},
    {"id": 5, "name": "Полиус", "constellation": "Центавр", "is_visible": False, "radius": 1.3}
]
#Открываем файл и сохраняем в json
with open(file, 'w') as f:
    json.dump(data_about_stars_1, f)

#Переменная дла подсчёта кол-ва операций
count_of_operations = 0

#отображение звёзд
def display_all_stars():
    #Открываем файл
    with open(file, 'r') as f:
        #Загружаем данные о звёздах
        stars = json.load(f)
        print("\nВсе записи:")
        #Перебор объектов и запись в json
        for star in stars:
            print(json.dumps(star, ensure_ascii = False, indent = 4))

#поиск по ID
def find_star_by_id(ID):
    #Открываем файл для чтения
    with open(file, 'r') as f:
        #Загружаем данные о звёздах
        stars = json.load(f)
        #Перебор списка звёзд для поиска необходимой (по ID) + проверки и вывод
        for index, star in enumerate(stars):
            if star['id'] == ID:
                print(f"\nЗапись найдена (позиция {index + 1}):")
                print(json.dumps(star, ensure_ascii = False, indent = 4))
                return True
        print("Запись не найдена.")
        return False

#Добавление новой звезды
def add_star():
    #Создаем пустой словарь для новой звезды
    new_star = {}
    
    while True:
        try:
            #Ввод данных
            new_star['id'] = int(input("Введите ID записи: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректный числовой ID.")
    
    new_star['name'] = input("Введите название звезды: ")
    new_star['constellation'] = input("Введите название созвездия: ")
    
    while True:
        is_visible_input = input("Можно ли увидеть звезду без телескопа (True/False): ")
        if is_visible_input in ['True', 'False']:
            new_star['is_visible'] = is_visible_input == 'True'
            break
        else:
            print("Пожалуйста, введите 'True' или 'False'.")
    
    while True:
        try:
            new_star['radius'] = float(input("Введите солнечный радиус звезды: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число для радиуса.")
    
    #Открываем файл и загружаем текущие данные
    with open(file, 'r') as f:
        stars = json.load(f)
    
    if any(star['id'] == new_star['id'] for star in stars):
        print("Запись с таким ID уже существует.")
        return
    
    #Добавляем новую звезду в список
    stars.append(new_star)

    #Открываем файл и сохраняем текущий список
    with open(file, 'w') as f:
        json.dump(stars, f)
    print("Запись добавлена.")

#Удаление по ID
def remove_star(ID_remove):
    #Открываем файл и загружаем данные
    with open(file, 'r') as f:
        stars = json.load(f)
    
    #если звезда найдена found = true
    found = False
    #перебор списка звёзд по ID с целью поиска необходимой
    for index, star in enumerate(stars):
        if star['id'] == ID_remove:
            del stars[index]
            found = True
            break

    if found:
        #Открываем файл и сохраняем список
        with open(file, 'w') as f:
            json.dump(stars, f)
        print("Запись удалена.")
    else:
        print("Запись не найдена.")

#Основной цикл
while True:
    #Меню
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")

    #Выбор опции
    user_choice = input("Выберите пункт меню: ")

    #Если 1
    if user_choice == '1':
        #Вывод всех звёзд
        display_all_stars()
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если 2
    elif user_choice == '2':
        while True:
            try:
                #Ввод ID
                ID = int(input("Введите ID записи для поиска: "))
                #Поиск по ID
                find_star_by_id(ID)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                print("неверный ID")

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
                #Ввод ID
                ID_remove = int(input("Введите ID записи для удаления: "))
                #Удаление по ID
                remove_star(ID_remove)
                #Счётчик операций увеличивается на 1
                count_of_operations += 1
                break  
            except ValueError:
                print("неверный ID")

    #Если 5
    elif user_choice == '5':
        #Ввод кол-ва операций
        print(f"Количество выполненных операций: {count_of_operations}")
        #Выход
        break  
    else:
        print("Неверное значение")

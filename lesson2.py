# Task 1

print("Task 1")
list_1 = ['my list', 1000.432, 78787, -366, 'new el', 334, 'test', 0]  # создаем список
print(f'Список: {list_1}')
for k in list_1:
    print(f'Элемент в списке {k} - имеет тип {type(k)}')

print()

# Task 2
print("Task 2")

# создаем список
list_2 = input('Введите элементы списка через пробел: ').split()
print('Ваш список: ')
print(list_2)

k = len(list_2)  # считаем количество элементов

# меняем местами
for n in range(1, k, 2):
    el = list_2.pop(n)
    list_2.insert((n - 1), el)
    n += 2

print('Поменяли элементы: ')
print(list_2)

print()

# Task 3
print("Task 3")

# создаем словарь времени года и месяцев
dict_season = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}

month = input('Введите номер месяца: ')  # запрашиваем месяц

# проверяем введенное значение
while not (month.isdigit() and int(month) in range(1, 13)):
    print('Вы ввели неправильное значение.')
    month = input('Попробуйте еще раз. Введите номер месяца: ')
else:
    month = int(month)

# выводим результат
print(f'Этот месяц относится ко времени года {dict_season.get(month)}.')

print()

# Task 4
print("Task 4")

# создаем список
list_3 = input('Введите вашу строку из нескольких слов, разделенных пробелами: ').split()

# выводим слова с новой строки
for i, val in enumerate(list_3, 1):
    print(i, val[:10])

print()

# Task 5
print("Task 5")

# создаем изначальный лист
list_4 = [9, 4, 2]

# запрашиваем новый элемент у пользователя
el = input('Введите натуральное число: ')

# проверяем введенное значение
while not (el.isdigit() and int(el) > 0):
    print('Вы ввели неправильное значение.')
    el = input('Попробуйте еще раз. Введите натуральное число: ')
else:
    el = int(el)
    k = len(list_4)  # мерим длину списка
    if el > list_4[0]:  # сравниваем с началом списка
        list_4.insert(0, el)
        print(f'Новый рейтинг: {list_4}')

    elif el <= list_4[k - 1]:  # сравниваем с концом списка
        list_4.append(el)
        print(f'Новый рейтинг: {list_4}')

    else:  # сравниваем со следующим элементом
        for i in range(k):
            if el > list_4[i + 1]:
                list_4.insert(i + 1, el)
                print(f'Новый рейтинг: {list_4}')
                break

print()

# Task 6
print("Task 6")

q = 'Y'

list_keys = ['название:', 'цена:', 'количество:', 'ед.:']
all_goods = []
list_names = []
list_prices = []
list_amounts = []
list_units = []

i = 0
while q != 'N':  # спрашиваем данные, пока пользователь хочет их вводить
    i += 1
    list_goods = []  # обнуляем список для нового товара

    name = input('Введите название товара: ')  # запрос названия товара
    list_goods.append(name)  # добавляем в список товара
    list_names.append(name)  # добавляем в список имен

    price = input('Введите цену товара: ')  # запрос цены товара
    while not (price.replace('.', '', 1).isdecimal() and float(price) > 0):  # проверяем введенную цену
        print('Вы ввели неправильное значение.')
        price = input('Попробуйте еще раз. Введите цену товара: ')
    else:
        price = float(price)
        list_goods.append(price)  # добавляем в список товара
        list_prices.append(price)  # добавляем в список цен

    amount = input('Введите количество товара: ')  # запрос количества товара
    while not (amount.isdecimal() and int(amount) > 0):  # проверяем введенное значение
        print('Вы ввели неправильное значение.')
        amount = input('Попробуйте еще раз. Введите количество товара: ')
    else:
        amount = int(amount)
        list_goods.append(amount)  # добавляем в список товара
        list_amounts.append(amount)  # добавляем в список количеств

    unit = input('Введите единицу измерения товара: ')  # запрос ед.измерения
    list_goods.append(unit)  # добавляем в список товара
    list_units.append(unit)  # добавляем в список ед.измерения

    dict_goods = dict(zip(list_keys, list_goods))  # создаем словарь со значениями товара
    tuple_goods = (i, dict_goods)  # создаем кортеж с номером и значениями товара
    all_goods.append(tuple_goods)  # добавляем кортеж в список

    q = input('Хотите ввести данные еще одного товара? Y/N: ')

print()
print('Структура:')
for n in all_goods:
    print(n)

print()
list_all = [list_names, list_prices, list_amounts, list_units]
dict_all = dict(zip(list_keys, list_all))  # создаем словарь аналитики
print('Аналитика')
for k in dict_all:
    print(f'{k} {dict_all[k]}')

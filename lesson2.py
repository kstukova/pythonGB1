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
while isinstance(month, int) is False:
    if not month.isdigit():
        print('Вы ввели неправильное значение.')
        month = input('Попробуйте еще раз. Введите номер месяца: ')
    elif int(month) not in range(1, 13):
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
list_3 = input('Введите вашу строку: ').split()

# выводим слова с новой строки
for i, val in enumerate(list_3, 1):
    print(i, val[:10])

print()

# Task 5
print("Task 5")

pros = float(input('Введите выручку: ')) # выручка
cost = float(input('Введите убыток: ')) # издержки
res = pros - cost # прибыль

if res > 0:
    print(f'Фирма получает прибыль. Рентабельность составляет {res / pros:.2f}')
    n = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {res / n:.2f}')
else:
    print(f'Фирма не получает прибыли.')

print()

# Task 6
print("Task 6")

a = float(input('Введите результат пробежки в 1-ый день, км: '))
b = float(input('Введите желаемый результат, км: '))

k = 1

while a < b:
    a = a + 0.1 * a
    k = k + 1
    print(f'{k}-й день: {a:.2f}')

print()
print(f'На {k}-й день спортсмен достигнет результата не менее {b} км')

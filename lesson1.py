# Task 1

print("Task 1")
name = input("Введи своё имя: ")
age = int(input("Введи свой возраст: "))
print("Привет, %s!" % name)
if age >= 18:
    print("Ты уже взрослый(ая). Тебе можно пить пиво!")  # если совершеннолетний
else:
    print(f"Тебе {age} лет. Тебе пока нельзя пить пиво!")  # если несовершеннолетний

print()

# Task 2
print("Task 2")

time = int(input('Введите время в секундах: '))
hours = time // 3600
mins = int((time % 3600) / 60)
secs = time - (hours * 3600) - (mins * 60)
print(f'Время в формате чч:мм:сс: {hours}:{mins}:{secs}')

print()

# Task 3
print("Task 3")

k = 1
m = 0
n = input('Введите число n: ')

while k < 4:
    m = int(k * n) + m
    k = k + 1

print(f'Сумма n + nn + nnn = {m}')

print()

# Task 4
print("Task 4")

k = 0
n = input('Введите целое положительное число: ')
dl = len(n) # длина строки
m = 0

while k < dl:
    if m < int(n[k]):
        m = int(n[k])
    k = k + 1

print(f'Самая большая цифра в числе = {m}')

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

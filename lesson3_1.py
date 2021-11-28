print('Task 1')
print()


def ksu_func(a, b):
    try:
        print(f'Результат деления a/b = {float(a) / float(b):.3f}')
    except ValueError:
        return print('Вы ввели не числа!')
    except ZeroDivisionError:
        return print('Нельзя делить на ноль!')


q = 'Y'
while q != 'N':
    ksu_func(input('Введите число a: '), input('Введите число b: '))
    q = input('Хотите посчитать еще? Y/N: ')

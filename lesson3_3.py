print('Task 3')
print()


def my_func(a, b, c):
    """Принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов."""
    try:
        x = [float(a), float(b), float(c)]
    except ValueError as err:
        print(f'Ошибочка! {err}')
    else:
        print(f'Сумма 2-х наибольших чисел = {round(sum(x) - min(x), 2)}')


q = 'Y'
while q != 'N':
    my_func(input('Введите 1-е число: '), input('Введите 2-е число: '), input('Введите 3-е число: '))
    q = input('Хотите посчитать еще? Y/N: ')

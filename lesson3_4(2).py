print('Task 4')
print()
#  вариант 2


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return print('Введенные числа не соответствуют условию!')
    except ValueError as err:
        print(f'Ошибочка! {err}')
    else:
        res = 1
        for i in range(abs(y)):
            res *= x
        print(f'x ^ y = {1 / res}')


q = 'Y'
while q != 'N':
    my_func(input('Введите x - действительное положительное число: '), input('Введите y - целое отрицательное число: '))
    q = input('Хотите посчитать еще? Y/N: ')

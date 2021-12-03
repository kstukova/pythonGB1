from math import factorial


def fact(k):
    for x in range(1, k+1):
        print(f'{x}! = ', end='')
        yield factorial(x)


n = input('Введите целое положительное число: ')
if n.isdigit() and int(n) > 0:
    n = int(n)
    for el in fact(n):
        print(el)
else:
    print('Введите целое неотрицательное число!')

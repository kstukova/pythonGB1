from itertools import count
from itertools import cycle


def gener_int():
    """ Генерирует целые числа, начиная с указанного и заканчивая указанным """
    try:
        n = int(input('С какого числа начать? '))
        m = int(input('До какого числа генерировать? '))
        if n >= m:
            return print('Первое число должно быть больше второго!')
    except ValueError:
        return print('Что-то не то ввели!')
    else:
        for el in count(n):
            if el > m:
                break
            else:
                print(el)


gener_int()
print()


def gener_str():
    """ Генерирует элементы из списка заданное количество раз """
    try:
        n = input('Введите список для генерации? ')
        m = int(input('Сколько раз сгенерировать? '))
        if m <= 0:
            return print('Количество генераций должно быть больше нуля!')
    except ValueError:
        return print('Что-то не то ввели!')
    else:
        i = 1
        for el in cycle(n):
            if i > m:
                break
            else:
                print(el, end='')
                i += 1


gener_str()

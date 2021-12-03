from sys import argv

salary_script, hours, rate, bonus = argv


def salary_func(h, r, b):
    try:
        h = float(h)
        r = float(r)
        b = float(b)
        if h < 0 or r < 0 or b < 0:
            return print('Вы ввели отрицательные значения!')
    except (ValueError, TypeError):
        return print('Вы ввели некорректные значения!')
    return print(f'Зарплата сотрудника: {h * r + b:.2f}')


salary_func(hours, rate, bonus)

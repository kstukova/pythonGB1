def func_unique_num():
    try:
        list1 = list(map(float, input('Введите список чисел через пробел: ').split()))
    except ValueError:
        print('Вы что-то не то ввели!')
    else:
        new_list = [el for el in list1 if list1.count(el) == 1]
        print(f'\nСписок уникальных чисел: {new_list}')


func_unique_num()

def func_bigger_num():
    try:
        list1 = list(map(float, input('Введите список чисел через пробел: ').split()))
    except ValueError:
        print('Вы что-то не то ввели!')
    else:
        new_list = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
        print(f'\nСписок чисел со значениями больше предыдущих: {new_list}')


func_bigger_num()

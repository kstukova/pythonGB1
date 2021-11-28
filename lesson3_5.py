print('Task 5')


def my_func():
    sum1 = 0
    try:
        user_list = list(map(float, user_string.split()))
        sum1 = sum(user_list)
        print(f'текущий ввод, сумма: {sum1}')
        return sum1
    except ValueError:
        print('Вы что-то не то ввели!')
        user_list = user_string.split()
        for i in range(len(user_list)):
            try:
                sum1 += float(user_list[i])
            except ValueError:
                pass
        print(f'текущий ввод, сумма: {sum1}')
        return sum1


print('\nДля завершения ввода введите q и нажмите Enter!\n')
full_sum = 0
while True:
    user_string = input('Введите числа через пробел: ')
    if user_string.find('q') != -1:
        user_string = user_string[0:user_string.find('q')]
        full_sum = full_sum + my_func()
        print(f'общая сумма: {full_sum}\n')
        break
    else:
        full_sum = full_sum + my_func()
        print(f'общая сумма: {full_sum}\n')

print('Task 2')
print()


def user_data(**kwargs):
    return kwargs


print(user_data(name=input('Введите имя: '), surname=input('Введите фамилию: '),
                year_of_birth=input('Введите год рождения: '), city=input('Введите город: '),
                email=input('Введите email: '), mobile=input('Введите номер телефона: ')))

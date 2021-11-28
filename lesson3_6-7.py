print('Task 6-7')
print()


def int_func(x):
    """Проверяет, состоит ли слово из маленьких латинских букв."""
    if (x.isascii() and x.isalpha() and x.islower()) is True:
        return x.title()


new_list = []
user_list = list(input('Введите слова из маленьких латинских букв: ').split())
for i in range(len(user_list)):
    if int_func(user_list[i]) is not None:
        new_list.append(int_func(user_list[i]))

if not new_list:
    print('Вы не ввели правильных значений!')
else:
    print(new_list)

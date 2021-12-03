from functools import reduce


def func_mult(x1, x2):
    return x1 * x2


even_list = [el for el in range(100, 1001) if el % 2 == 0]
even_mult = reduce(func_mult, even_list)
print(even_mult)

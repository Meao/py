# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2

def get_fib_nums_lst(n):
    """
    n - количество чисел в списке 

    """
    if isinstance(n, int):
        if n == 0:
            return None
        fib_lst = []
        fib_lst = list(fibonacci(n))
    else:
        return None
    return fib_lst


assert get_fib_nums_lst(0) is None, "неверный аргумент n"

assert get_fib_nums_lst('0') is None, "неверный аргумент n"

assert get_fib_nums_lst(1) == [0], "ряд начинается с 0"
assert get_fib_nums_lst(2) == [0, 1], "ряд длины 2"
assert get_fib_nums_lst(3) == [0, 1, 1], "ряд длины 3"

assert get_fib_nums_lst(5) == [0, 1, 1, 2, 3], "ряд длины 5"

assert get_fib_nums_lst(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "ряд длины 10"

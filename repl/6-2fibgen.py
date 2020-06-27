# На основе кода, предоставленного преподавателем, реализовать генератор чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с помощью генератора списков, с помощью функции, внутри которой yield.
import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if inner.called >= 0:
            print("Запускаем foo")
            # func.called = () # Сравнить работу once в случае
            # сохранения внутри func и внутри inner
            res = (func(*args, **kwargs))
            inner.called += 1
            print(inner.called)
        return res

    # print('init')
    inner.called = 0  # ?
    return inner


@once
def foo():
    """
    docs for foo
    """
    # [0, 1, 1, 2, 3, 5, 8, 13]
    # то, что у вас должно возвращать очередной
    # элемент ряда Фибоначчи
    cur_el = 0
    # если foo - вызывается впервые, то возвращаем 0
    # а если во второй раз, то 1
    # обычная ситуация
    # cur_el = prev_el + prev_prev_el
    prev_prev_el, prev_el = 0, 1
    while True:
        return prev_prev_el
        # yield prev_prev_el
        current = prev_prev_el + prev_el
        prev_prev_el = prev_el
        prev_el = current
    return cur_el


# print("Очередное число ряда Ф.", foo())
# print("Очередное число ряда Ф.", foo())
# print("Очередное число ряда Ф.", foo())
# print("Очередное число ряда Ф.", foo())



def foo_gen():
    """
        Функция, которая возвращает по одному значения из ряда Фибоначчи
    """
    # [0, 1, 1, 2, 3, 5, 8, 13]
    prev_prev_el = 0
    second = 1    

    yield prev_prev_el # 1 эл-т ряда Ф.

    yield second # 2 эл-т ряда Ф. 

    while True:
        current = prev_prev_el + second
        yield current
        prev_prev_el, second = second, current

    

fib_lst = foo_gen()
    
print(next(fib_lst))
print(next(fib_lst))
print(next(fib_lst))
print(next(fib_lst))
print(next(fib_lst))
print(next(fib_lst))
print(next(fib_lst))



        



     


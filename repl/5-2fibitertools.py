# Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).

from itertools import count, islice


def fib(n):
    n = int(n)
    if n > 0:
        if n == 1:
            res = [0]
            return res
        elif n > 1:
            res = [0, 1, ]
            for i in islice(count(2), n-2):
                res.append(res[i - 1] + res[i - 2])
            return res
    else:
        res = 'Enter a positive integer'
        return res

def inputn():
    print('How many fibonacci elements to list?\n')
    while True:
        try:
            n = input("Please enter an integer: ")
            n = int(n)
            return n
        except ValueError:
            print("Not a valid integer! Please try again ...")


if __name__ == "__main__":
    # 
    # n = input()
    n = inputn()
    print('Result')
    print(fib(n))

# На основе кода, предоставленного преподавателем, реализовать генератор чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с помощью генератора списков, с помощью функции, внутри которой yield.

def fib(n):
    n = int(n)
    if n > 0:
        series=[]
        series.append(0)
        series.append(1)
        [series.append(series[k-1]+series[k-2]) for k in range(2,n)]
        return series
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
    n = inputn()
    print('Result')
    print(fib(n))

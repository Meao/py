"""
Кривцун ИВТ3
ПРОГ-5 Тема 2. Итераторы Инвариантная СР (ИСР)
2.1. Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.

2.2. Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.

2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
"""
def fib():
    """
    Fibonacci 2.1.
    Takes 0 arguments
    Outputs a line of integers
    """
    fib0 = 0
    fib1 = 1
    print('Type max value')
    max_val = int(input())
    if max_val < 0:
        print('Invalid input')
        return 0
    print(fib0, end=' ')
    while fib1<max_val:
        fib0, fib1 = fib1, fib0 + fib1
        print(fib0, end=' ')
 
fib()
print('\n')
print('\n')

class FList:                                        
    def __init__(self, max_val):                      
        self.max_val = max_val

    def __iter__(self):                           
        self.zero = 0
        self.first = 1
        # return self.inorder_iter()
        return self

    def __next__(self):                           
        fib = self.zero
        if fib > self.max_val:
            raise StopIteration                   
        self.zero, self.first = self.first, self.zero + self.first
        return fib   

    def __getitem__(self, i):
        if i > self.max_val:
            raise IndexError(i)
        return i

    def fiblist(self):
        """
        If I return a list, I map over the Iterable Object ATM. 
        Or else I'd need to call next(fl) several times after fl=FibList(max).
        But if I want a class to be aimed to return a list,
        into 
        def __init__(self, mazx):
            ...
            self.__fiblist__(self)
        Call fiblist __get_item__
        So to sum up, if I want to return a list, I need iter, next. 
        If I just return an iterable object, I need getitem.
        """
        fl = [self.zero, self.first]
        i = 0
        if fl[i] > self.max_val:
            raise StopIteration
        fl.append(fl[i-1] + fl[i])
        fl.append(fib)
        i += 1
        return fl
 

for n in FList(10):
  print (n, end=" ")

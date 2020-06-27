'''
Krivtson Marina IVT2.3

реализовать получение уникальных элементов так, чтобы внутрь функции unique_func можно было передать не только один итерабл (iterable) объект типа list, но и любые другие элементы типа float, int и т. д. Используйте распаковку и упаковку элементов.

Например:

    unique_func(1, [2,3,3,4], 'string', (10,9,8)) # должно получиться [1,2,3,4,'s','t','r','i','n','g',10,9,8]
    unique_func([2,3,4,5],[5,0],seen=[1]) # должно получиться [1,2,3,4,5,0]
'''

from collections.abc import Iterable

def unique_func(*args, seen=[]):
    seen = set(seen)
    res = list(seen)
    for arg in args:
        if not isinstance(arg, Iterable):
            # checks whether the object arg is an instance of iterable objects
            if arg not in seen:
                seen.add(arg)
                res.append(arg)
        else:
            for i in arg:
                if i not in seen:
                    seen.add(i)
                    res.append(i)
    return res
    

print(unique_func(1, [2,3,3,4], 'string', (10,9,8)))
print(unique_func(1, [2,3,3,4], 'string', (10,9,8)))

if __name__ == '__main__':
    assert unique_func(1, [2,3,3,4], 'string', (10,9,8)) == [1,2,3,4,'s','t','r','i','n','g',10,9,8]
    assert unique_func([2,3,4,5],[5,0],seen=[1]) == [1,2,3,4,5,0]

def u_f(seen=set(), *lst):
    """
        Get one argument which is list - lst.
        Returns new list with unique elements 
    """
    for item in lst:
        if isinstance (item, Iterable):
            u_f(seen, *item) 
        else:
            seen.add(item) 
        # The add() method doesn't add an element to the set if it's already present in it otherwise it will get added to the set.
    return seen


lst = [1, 0, 0, 5, 0, 0]
s = {3, 0}
st = 'st'
 
def unique_f(lst, seen=None):
    """
        Get one argument which is list - lst.
        Returns new list with unique elements
        avoid non mutable things in () of a function 
    """
    seen = list(seen or [])
    return seen


lst = [1, 0, 0, 5, 0, 0]
s = {3, 0}

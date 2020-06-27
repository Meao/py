'''
Krivtson Marina IVT2.3
Напишите функцию, которая для заданного списка возвращает новый список из уникальных элементов, содержащихся во входном списке (на занятии 18.10.18, 20.10.18)

def unique_func(lst):
    """
        Get one argument which is list - lst.
        Returns new list with unique elements 
    
    """
    result_lst = []
    
    return result_lst
    
Функция unique_func возвращает список из уникальных элементов, которые мы ей передали. Для начала, мы будем передавать ей переменную в виде списка
'''
def unique_func(lst):
    """
        Get one argument which is list - lst.
        Returns new list with unique elements 
    
    """
    result_lst = list(set(lst))
    return result_lst
    
lst = [1, 0, 0, 5, 0, 0]
myset = unique_func(lst)
print(myset)

if __name__ == '__main__':
 assert unique_func([3,2,1,49,0])  ==  [0,1,2,3,49], "Напишите функцию, которая для заданного списка возвращает новый список из уникальных элементов, содержащихся во входном списке (на занятии 18.10.18, 20.10.18)"
 assert unique_func([2,3,3,4]) ==  [2,3,4]

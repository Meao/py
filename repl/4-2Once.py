""" 
Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
"""
import functools
#позволиить создать единожды подлючение к бд
def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called: 
            # func.called = () # Сравнить работу once в случае 
            # сохранения внутри func и внутри inner        
            res = func(*args, **kwargs)
            inner.called = True # ? 
            print('called is changed')
            return res
    
    print('init')       
    inner.called = False # при добавке декоратора к функции собачкой, создается функция иннер, также атрибут колд создается и ему присваивается это значение, этакая мета-информация
    return inner

@once
def strfunc(inp_string, offset):
    res_list = []
    
    d = {}
    for c in (65, 97):  
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
        
    res_list = [d.get(c, c) for c in inp_string]

    res_string = ''.join(res_list)
    return res_string
    
  

my_str = "How can you tell an extrovert from an introvert at NSA? In the elevators, the extrovert looks at the OTHER guy's shoes." # TODO 

res_str = strfunc(my_str, 13)

print(res_str)
res_str = strfunc(my_str, 13)

print(res_str)



""" 
Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
"""

def strfunc(inp_string, offset):
    res_list = []
    
    d = {}
    for c in (65, 97):  
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    # for ch in inp_string:  # TODO 
        # res_list.append(ord(ch))
        
    res_list = [d.get(c, c) for c in inp_string]
    # print("".join([d.get(c, c) for c in inp_string]))

    res_string = ''.join(res_list)
    return res_string
    
  

my_str = "How can you tell an extrovert from an introvert at NSA? In the elevators, the extrovert looks at the OTHER guy's shoes." # TODO 

res_str = strfunc(my_str, 13)

print(res_str)



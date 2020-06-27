'''
Krivtson Marina IVT2.3
 
Реализуйте программу с реализацией работы функции zip через функцию map.
'''
a1, a2, a3 = 'abcd',(10, 20, 30),[3,4,6]
print(list(map(lambda *args: args, a1, a2, a3)))

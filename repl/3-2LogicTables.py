
# Кривцун Марина, группа ИВТ2-3

# 21.09.2018, Лабораторная работа 2
# Нужно сделать: конъюнкция, дизъюнкция и импликация
"""
 выводить таблицы истинности для трех операций: конъюнкция, дизъюнкция и импликация
"""

print('Отрицание')
print('–'*6)
print(chr(124) + "A"+chr(124)+ chr(172)+'A' + chr(124))
a = True
print(chr(124)+str(int(a))+chr(124)+str(int(not a))+chr(124))
a = False
print(chr(124)+str(int(a))+chr(124)+str(int(not a))+chr(124))
print('–'*6)

print ('\n''Конъюнкция')
print('–'*8)
print(chr(124) + "A"+chr(124)+'B' + chr(124)+'A∧B')
a = True
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a&b))+chr(124))
a = True
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a&b))+chr(124))
a = False
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a&b))+chr(124))
a = False
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a&b))+chr(124))
print('–'*8)

print ('\n''дизъюнкция')
print('–'*8)
print(chr(124) + "A"+chr(124)+'B' + chr(124)+'AUB')
a = True
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a or b))+chr(124))
a = True
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a or b))+chr(124))
a = False
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a or b))+chr(124))
a = False
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int(a or b))+chr(124))
print('–'*8)

print ('\n''импликация')
print('–'*8)
print(chr(124) + "A"+chr(124)+'B' + chr(124)+'A->B')
a = True
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int((not a) or b))+chr(124))
a = True
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int((not a) or b))+chr(124))
a = False
b = True
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int((not a) or b))+chr(124))
a = False
b = False
print(chr(124)+str(int(a))+chr(124)+str(int(b))+chr(124)+str(int((not a) or b))+chr(124))
print('–'*8)

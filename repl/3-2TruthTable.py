# Кривцун Марина, группа ИВТ2-3
# Вариант: 16

# Описание задачи

  # Постройте таблицу истинности для: 16.	¬B→C∧B∨(¬C→B)___________________________________________________________________
print ('\n''F=¬B→C∧B∨(¬C→B)')
print('–'*8)
print(chr(124) + "B"+chr(124)+'C' + chr(124)+'F'+chr(124))
b = True
c = True
print(chr(124)+str(int(b))+chr(124)+str(int(c))+chr(124)+str(int(not (not b) or (c&b or (not (not c) or b))))+chr(124))
b = True
c = False
print(chr(124)+str(int(b))+chr(124)+str(int(c))+chr(124)+str(int(not (not b) or (c&b or (not (not c) or b))))+chr(124))
b = False
c = True
print(chr(124)+str(int(b))+chr(124)+str(int(c))+chr(124)+str(int(not (not b) or (c&b or (not (not c) or b))))+chr(124))
b = False
c = False
print(chr(124)+str(int(b))+chr(124)+str(int(c))+chr(124)+str(int(not (not b) or (c&b or (not (not c) or b))))+chr(124))
print('–'*8)
  

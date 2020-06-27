# Кривцун Марина, группа ИВТ2-3

# Номер варианта	Задание №1	Задание №3
# 4	5, 7, 18	16, 22
# Задание 1. Логическая задача. Требуется для двух или трех входных переменных (A, B, C) построить таблицы истинности 5. (A∨B)∧ ¬C 7. (A→B)∧A) ↔ A∧B 18. A∨(B∧C)↔(A∨B)∧(A∨C) 
# Задание 2. Используя конкатенацию строк, функцию print(), а также умножение строки на число, создайте оформление для таблиц истинности, созданных в рамках предыдущего задания.
# Задание 3. Дан список: 
lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
# Для данного списка, используя слайсы, обращение к элементам по индексу (не используя циклы или условные операторы) найдите: 16. Сумму элементов, стоящих на четных местах списка с минимальным элементом этого списка.
# Дан кортеж:

car = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230, "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)

# найдите: 22. Список названий полей (name, n_of_wheels, ...)

# Задание 1 & 2
from inspect import signature

def printSeparator(fill, title, size):
  print ('{t:{f}^{s}}'.format(t=title, f=fill, s=size))

# Prints a truth table for f(A, B) or f(A, B, C)
# title will appear in header (--------title-------)
# fname is the last column name (A   B   fname)
def printTable(f, title, fname):
  argc = len(signature(f).parameters) # check how many parameters function f has
  printSeparator('-', title, 33)
  header = 'A  B  ' + ('C  ' if argc == 3 else '') + fname
  print (header)
  if argc == 2:
    printTableAB(f)
  elif argc == 3:
    printTableABC(f)
  else:
    print ('Error! Provide a function that takes 2 or 3 arguments.')
  printSeparator('-', '', 33)

# Helper function, prints the truth table body for function f(A, B)
def printTableAB(f):
  for A in (0, 1):
    for B in (0, 1):
        print ('%d  %d  %s' % (A, B, bool(f(A, B))))


# Helper function, prints the truth table body for function f(A, B, C)
def printTableABC(f):
  for A in (0, 1):
    for B in (0, 1):
      for C in (0, 1):
          print ('%d  %d  %d  %s' % (A, B, C, bool(f(A, B, C))))


# lambda is just an anonymous function, could do something like
# def f5(A, B, C):
#   return (A and B) or (not C)
# printTable(f5, "#5", "(A∨B)∧ ¬C")
# and it is equivalent to
# printTable(lambda A, B, C: (A and B) or (not C), "#5", "(A∨B)∧ ¬C")

print("Задание №1 и №2")
printTable(lambda A, B, C: (A and B) or (not C), "#5", "(A∨B)∧ ¬C")
printTable(lambda A, B: A or B, "#6", "A|B")
printTable(lambda A, B: ((not(A) or B) or A) is (A and B), "#7", "((A→B)∧A) ↔ A∧B")
printTable(lambda A, B, C: (A and (B or C)) is (A and B) or (A and C), "#18", "A∨(B∧C)↔(A∨B)∧(A∨C)")


# Задание 3

# Описание задачи

  # Дан список: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
  # Для данного списка, используя слайсы, обращение к элементам по 
  # индексу, методы sum(), min(), max(), арифметические операторы (не используя циклы или условные операторы) найдите:
  
  # 10. Отрицательное значение последнего элемента из элементов 
  # первой половины списка. 
   

print ('\n' 'Задание №3' '\n\n''№3')
list=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946]
print ('Список: ', list)
print ('\n''Отрицательное значение последнего элемента из элементов первой половины списка: ','-',list[len(list)//2])
print ('\n''Сумма элементов, стоящих на четных местах списка с минимальным элементом этого списка: ','-',list[len(list)//2])
#55 должно быть print ('\n''Сумма элементов, расположенных на четных позициях, первой половины списка: ',sum(list[1:len(list)//2:2]))

  # Дан кортеж: ("name", " DeLorean DMC-12", "motor_pos": "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230, "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)
  
  # Для данного кортежа, используя слайсы, обращение к элементам по 
  # индексу, методы sum(), min(), max(), арифметические операторы (не используя циклы или условные операторы) найдите:

# 22.	Список названий полей (name, n_of_wheels, …) 
print ('\n' '22.')
tuple = ("name","DeLorean DMC-12","motor_pos","rear","n_of_wheels",4,"n_of_passengers",2,"weight",1.230,"height",1.140,"length",4.216,"width",1.857,"max_speed",177)
print ('Кортеж: ', tuple )
print ('\n' 'Список названий полей (name, n_of_wheels, ...): ''\n',tuple[::2])

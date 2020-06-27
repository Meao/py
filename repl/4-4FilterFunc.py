"""
Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).
"""
from random import randint

def random_numbers(length):
  numbers = []
  
  for i in range(length):
    numbers.append(randint(-50, 50))
  
  return numbers


def split_list(lst, filter_func):
  passes_filter = []
  rejected = []

  for val in lst:
    if filter_func(val):
      passes_filter.append(val)
    else: rejected.append(val)
  
  return {"passes filter": passes_filter, "doesn't pass filter": rejected}


l = random_numbers(20)
# четность/нечетность
print(split_list(l, lambda x: x < 0))
# положительные/отрицательные
print(split_list(l, lambda x: x % 2 == 0))

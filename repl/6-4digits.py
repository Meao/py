'''
Написать программу, в которой пользователь вводит число от 0 до 9 включительно, а программа выводит название введённого числа, а если второй входной аргумент type имеет значение bin, oct, hex, то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму. Предусмотреть проверку корректности введённого пользователем значения. 
'''
def foo(digit, to_type=None):
    if digit.isdigit():
        if to_type:
            return convert(digit, to_type)
        else:
            return num(digit)
    else:
        return 'Not a digit'

def num(digit):        
    digits = {
        '0': 'Ноль',
        '1': 'Один',
        '2': 'Два',
        '3': 'Три',
        '4': 'Четыре',
        '5': 'Пять',
        '6': 'Шесть',
        '7': 'Семь',
        '8': 'Восемь',
        '9': 'Девять',
        }
    return digits[digit]

def convert(digit, to_type=None): 
    types = {
        'bin': '{:b}',
        'oct': '{:o}',
        'hex': '{:x}'
        }
    digit = int(digit)
    if to_type in types.keys():
        return types[to_type].format(digit)
    else:
        return 'Not a valid conversion type'


# print(foo(digit='2', to_type='bin'))
# print(foo(digit="9", to_type='oct'))
# print(foo(digit='3', to_type='hex'))
# print(foo(digit='4'))
# print(foo(digit='5'))

digit = input('Введите цифру от 0 до 9\n')
to_type=None
to_type = input('Введите, при желании,  форму вывода bin, oct или hex\n')

print(foo(digit, to_type))

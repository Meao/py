"""
Кривцун ИВТ2

Реализуйте основу для работы калькулятора (несколько функций для вычисления основных операций). Сопроводите документацией и протестируйте их работу. 

Обдумайте как наиболее вероятно модифицировать код в дальнейшем, чтобы калькулятор мог принимать неограниченное количество операндов и типов действий (операции). 
"""

def mu(o1, o2):
    """
    Multiply
    Takes 2 arguments
    Outputs 1 result
    """
    return o1*o2

def di(o1, o2):
    """
    Divide
    Takes 2 arguments
    Outputs 1 result
    """
    return o1/o2

def su(o1, o2):
    """
    Sum 
    Takes 2 arguments
    Outputs 1 result
    """
    return o1+o2

def sub(o1, o2):
    """
    Substarct
    Takes 2 arguments
    Outputs 1 result
    """
    return o1-o2

def log_res(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('test.txt', 'w') as f:
            f.write(str(result))
        return result

    return wrapper


@log_res
def Calc():
    """
    Calculator
    Prompts for input, creates operands and operator, calls functions to calculate expression.
    """
    print('Please type a maths expression with 2 intergers or floats and an operator "+", "-", "*" or "/"')
    inp = (input())
    for char in inp:
        if char not in '1234567890.-+*/':
            print('Please restart the program and only type valid characters')
            return
    operators = ["+", "-", "*", "/"]
    buf = ''
    operand1 = 0.0
    operand2 = 0.0
    for char in inp:
        if char not in operators:
            buf += char
        else:
            operator = char
            operand1 = float(buf)
            buf = ''
    operand2 = float(buf)
    res = 0.0
    if operator == '+':
        res = su(operand1, operand2)
    elif operator == '-':
        res = sub(operand1, operand2)
    elif operator == '*':
        res = mu(operand1, operand2)
    elif operand2==0:
        return "Can not divide by 0"
    else:
        res = di(operand1, operand2)
    print(res)
    return res


Calc()

if __name__ == '__main__':
    assert mu(4, 5) == 20
    assert di(4, 2) == 2
    assert su(4, 5) == 9
    assert sub(4, 5) == -1

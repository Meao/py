# Krivcun IVT2-3
# 2.1. Разработать прототип программы "Калькулятор", позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.  [ без использования '@' ]
# 2.2. Дополнение программы "Калькулятор" декоратором, сохраняющим выполняемые действия, в файл-журнал. 
# 2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
def calcul21():
    s = input("Enter an operation sign (+,-,*,/): ")
    if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            title = 'Sum'
            r = x + y
            print("%.2f" % (r))
            return title, x, y, r
        elif s == '-':
            title = 'Difference'
            r = x - y
            print("%.2f" % (r))
            return title, x, y, r
        elif s == '*':
            title = 'Multiplication'
            r = x * y
            print("%.2f" % (r))
            return title, x, y, r
        elif s == '/':
            title = 'Division'
            if y != 0:
                r = x / y
                print("%.2f" % (r))
                return title, x, y, r
            else:
                r = "Division by 0."
                print(r)
                return title, x, y, r
    else:
        print("I don't recognise your input.")
        res = calcul21()
        return res

def deco(res):
    f = open("text.txt","a+")
    f.write(str(res[0])+' of '+str(res[1])+' and '+str(res[2])+' is '+str(res[3])+'\n')
    f.close()

deco(calcul21())

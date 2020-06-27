'''
Krivtson Marina IVT2.3
'''
var = 100500

def factorial(number):
  if type(number) is int:
    if number == 0:
      return 1
    elif number >=1:
      return number * factorial(number-1)


def test_float_val(n):
  assert factorial(n) == None, "Factorial of {n}"

def test_negative_val(n):
  assert factorial(n) == None, "Factorial of {n}"

def test_min_val(n):
  assert factorial(n) == 1, "Factorial of {n}"

test_float_val(1.1)
test_negative_val(-1)
test_min_val(0)

print (factorial(5))

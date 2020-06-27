#Кривцун Марина ИВТ2
import math


def logfoo():
    n = 2  #loop number
    u = 0.5  #element Un
    sums = 0.5  #resulting sum S
    x = 0.5
    e = 0.0001  #epsilon
    while abs(u) >= e:
        m = (-x * (n - 1)) / n
        u = u * m
        sums = sums + u
        n = n + 1
    return sums


def arctanfoo():
    n = 1
    u = 0.52
    sums = 0.52
    x = math.pi / 6
    exp = 0.0001
    while abs(u) >= exp:
        m = (-x * x * (2 * n - 1)) / (2 * n + 1)
        u = u * m
        sums = sums + u
        n = n + 1
    return sums


print('ln(x+1) = %.2f' % logfoo())
print('arctg(x) = %.2f' % arctanfoo())

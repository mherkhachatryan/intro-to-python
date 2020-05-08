from functools import partial
from math import sin

def sum(a, b, c, d):
    print('a=', a)
    print('b=', b)
    return a + b


add_three = partial(sum, 4, c=6)
print(add_three(5))


def ho(x, fun):
    return fun(x)


ho(0, sin)

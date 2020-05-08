
def decorator_func_(fun):
    def func_wrapper(self, a, b):
        return fun(self, a ** 2, b ** 2)

    return func_wrapper


def decorator_func(fun):
    def func_wrapper(self, *args, **kwargs):
        args = tuple(map(lambda x: x ** 2, args))
        return fun(self, *args, **kwargs)

    return func_wrapper


def decorate_any(fun_on_args):

    def _decorator_func(fun):
        def func_wrapper(self, *args, **kwargs):
            args = tuple(map(fun_on_args, args))
            return fun(self, *args, **kwargs)

        return func_wrapper
    return _decorator_func


class A:

    def add(self, a, b):
        return a + b

    @decorator_func_
    def add_sqrs(self, a, b):
        return a + b

    @decorator_func
    def add_all(self, a, b, c, d):
        return a + b + c + d

    @decorator_func
    @decorator_func
    def add_quads(self, a, b):
        return a + b

    @decorate_any(lambda x: x + 1)
    @decorator_func
    def prod_inc(self, a, b):
        return a * b


a_ = A()
print('1 + 2 = ', a_.add(1, 2))
print('1^2 + 2^2 = ', a_.add_sqrs(1, 2))
print('1^4 + 2^4 = ', a_.add_quads(1, 2))

print('(2 + 1) ** 2 * (3 + 1) ** 2 = ', a_.prod_inc(2, 3))

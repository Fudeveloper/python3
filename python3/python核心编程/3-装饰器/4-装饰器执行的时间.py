def decorate(fun):
    print('decorating')
    def wrapper():
        print('------')
    return fun

# 只要python解释器执行到了这个代码，那么就会自动进行装饰，而不是等到调用的时候
@decorate
def f1():
    print('f1')

# decorating
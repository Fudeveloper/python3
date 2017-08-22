def outside_func(args):
    def decorate(func):
        def wrapper():
            print('---log:args={0}---'.format(args))
            if args == 'haha':
                func()
                func()
            else:
                func()
        return wrapper
    return decorate


# 1.先执行outside_func('haha')这个方法，将这个方法return的函数指针作为装饰器
# 2.调用decorate
# 3.使用@decorate对函数进行装饰
@outside_func('haha')
def f1():
    print('---f1---')

f1()

# 带有参数的装饰器，能够在运行时起到不同的功能，提高代码复用性
@outside_func('xixi')
def f2():
    print('---f2---')

f2()


# ---log:args=haha---
# ---f1---
# ---f1---
# ---log:args=xixi---
# ---f2---
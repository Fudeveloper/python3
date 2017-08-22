def decorate(func):
    def wrapper(*args,**kwargs):
        print('--装饰--')
        return_value = func(*args,**kwargs)
        return return_value
    return wrapper

@decorate
def f1():
    print('---无参数无返回值---')

@decorate
def f2(a):
    print('---单个参数无返回值---')

@decorate
def f3(a,b,c):
    print('---多个参数无返回值---')

@decorate
def f4(a):
    print('---单个参数有返回值---')
    return 'f4'

@decorate
def f5(a,b,c):
    print('---多个参数有返回值---')
    return 'f5'

print(f1())
print(f2(1))
print(f3(2,3,4))
print(f4(4))
print(f5(5,6,7))


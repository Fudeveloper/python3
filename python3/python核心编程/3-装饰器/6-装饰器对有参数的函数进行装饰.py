def decoreate(func):
    def wrapper(x, y): # 如果形参x,y没有定义,将导致18行的调用失败
        print('---装饰---')
        func(x,y)   # 如果没有将x,y当作实参传递，那么会导致15行方法执行失败
    return wrapper

# 针对不定长度的参数
def decoreate2(func):
    def wrapper(*args,**kwargs):
        print('---装饰---')
        func(*args,**kwargs)
    return wrapper

@decoreate
def f1(a,b):
    print('a={0},b={1}'.format(a,b))

f1(1, 2)

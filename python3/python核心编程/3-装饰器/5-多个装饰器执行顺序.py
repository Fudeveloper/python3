# 装饰时是倒着装，真正执行时，还是从上往下



def b(fun):
    print('---装饰1---')
    def wrapper():
        print('---验证1---')
        return '<b>{0}</b>'.format(str(fun()))
    return wrapper

def i(fun):
    print('---装饰2---')
    def wrapper():
        print('---验证2---')
        return '<i>{0}</i>'.format(str(fun()))
    return wrapper


@b
@i      # 先调用最近的装饰器，再将装饰过的方法返回给上方装饰器
def f1():
    print('---3---')
    return 'hello'


print(f1())


# ---装饰2---
# ---装饰1---
# ---验证1---
# ---验证2---
# ---3---
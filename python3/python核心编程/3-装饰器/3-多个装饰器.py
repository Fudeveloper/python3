# 装饰时是倒着装，真正执行时，还是从上往下



def b(fun):
    def wrapper():
        print('---1---')
        return '<b>{0}</b>'.format(str(fun()))
    return wrapper

def i(fun):
    def wrapper():
        print('---2---')
        return '<i>{0}</i>'.format(str(fun()))
    return wrapper


@b
@i      # 先调用最近的装饰器，再将装饰过的方法返回给上方装饰器
def f1():
    print('---3---')
    return 'hello'


print(f1())

# # 原理
# f1 = i(f1)
# f1 = b(f1)
# print(f1())


# ---1---
# ---2---
# ---3---
# <b><i>hello</i></b>




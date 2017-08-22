class C1(object):
    def __init__(self,func):
        print('--装饰--')
        print(func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('--log--')
        self.__func()

@C1
def f1():
    print('---f1---')




f1()
# --装饰--
# f1
# # 上方是未调用f1()前（初始化方法的时候输出）
# --log--
# ---f1---


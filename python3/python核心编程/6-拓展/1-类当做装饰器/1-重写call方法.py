class C1(object):
    def __call__(self, *args, **kwargs):
        print('C1')

c = C1()
c()     #C1

# 重写call方法后，类的实例对象可以直接被调用

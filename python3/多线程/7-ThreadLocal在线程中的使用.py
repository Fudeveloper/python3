import threading

# 创建全局local对象
local = threading.local()


class Student(object):
    def __init__(self,name):
        self.name = name


class MyThread(threading.Thread):
    def __init__(self,stdname):
        # 完全初始化父类
        super(MyThread,self).__init__()
        self.stdname = stdname

    def run(self):
        local.student=Student(self.stdname)
        print(local.student.name)


mt1 = MyThread('dongdong')
mt2 = MyThread('xixi')
mt1.start()
mt2.start()
mt1.join()
mt2.join()


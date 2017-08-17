from threading import Thread
import time
g_num = 100


class MyThread(Thread):
    def run(self):
        global g_num
        for i in range(3):
            g_num += 1


class MyThread2(Thread):
    def run(self):
        global g_num
        print('g_num={0}'.format(g_num))

t1 = MyThread()
t2 = MyThread2()

t1.start()
t2.start()

# g_num=103
import threading
from threading import Thread

g_num = 0
# 创建锁
lock = threading.Lock()


def fun1():
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num += 1
        lock.release()
    print('g_num={0}'.format(g_num))


def fun2():
    global g_num
    for i in range(100000):
        lock.acquire()
        g_num += 1
        lock.release()
    print('g_num={0}'.format(g_num))

t1 = Thread(target=fun1)
t1.start()
t2 = Thread(target=fun2)
t2.start()

t1.join()
t2.join()
print(g_num)




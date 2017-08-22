# 同步的概念：协同步调，按预定的先后顺序运行
from threading import Thread
from threading import Lock


class MyThread1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('mythread-1')
                lock2.release()


class MyThread2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('mythread-2')
                lock3.release()


class MyThread3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('mythread-3')
                lock1.release()

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()

mt1 = MyThread1()
mt2 = MyThread2()
mt3 = MyThread3()


lock2.acquire()
lock3.acquire()

mt1.start()
mt2.start()
mt3.start()

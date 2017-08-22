# 异步概念：计算机多线程的异步处理。与同步处理相对，异步处理不用阻塞当前线程来等待处理完成，而是允许后续操作，直至其它线程将处理完成，并回调通知此线程。
import time
import os

from multiprocessing import Pool


def test():
    for i in range(3):
        print('此线程{0}，父线程{1}'.format(os.getpid(),os.getppid()))
        time.sleep(1 )
    return 'hhhh'


def test2(args):
    print('test2的参数{0}  此线程{1}'.format(args,os.getpid()))
    return 'test2'

pool = Pool(3)
pool.apply_async(func=test, callback=test2)

while True:
    time.sleep(1)
    print('---主线程---{0}'.format(os.getpid()))

# 此线程2296，父线程2294
# ---主线程---2294
# 此线程2296，父线程2294
# ---主线程---2294
# 此线程2296，父线程2294
# ---主线程---2294
# test2的参数hhhh  此线程2294
# ---主线程---2294
# ---主线程---2294
# ---主线程---2294

# 其中，26，28，30 行为进程池中3条进程执行输出，3条进程执行完后，将'hhhh'返回给执行回调函数的线程（即主进程，主进程一直在执行），。输出32时，主线程切换执行callback函数：test2。
from multiprocessing import Pool
import time
import random
import os

def worker(num):
    for i in range(3):
        print('pid=={0}  num={1}'.format(os.getpid(),num))

pool = Pool(3)
for i in range(10):
    # 非堵塞添加任务
    pool.apply_async(worker,(i,))
    # # 堵塞添加任务
    # pool.apply(worker,(i,))
pool.close()
pool.join()



from multiprocessing import Pool
from multiprocessing import Process
# 需要multiprocessing中的Queue，只能完成普通的队列通信
from multiprocessing import Queue
import time


def put(queue):
    for i in ['a', 'b', 'c']:
        queue.put(i)
        time.sleep(1)
        print('put {0} to queue'.format(i))


def get(queue):
    print(queue.qsize())
    while True:
        if not queue.empty():
            value = queue.get(True)
            print('get {0} from queue'.format(value))

if __name__ == '__main__':

    q = Queue()
    p1 = Process(target=put, args=(q,))
    p2 = Process(target=get, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

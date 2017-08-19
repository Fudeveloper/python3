from multiprocessing import Manager
from multiprocessing import Pool


def put(queue):
    for i in ['a', 'b', 'c']:
        queue.put(i)
        print('put {0} to queue'.format(i))


def get(queue):
    for i in range(queue.qsize()):
        value = queue.get()
        print('get {0} from queue'.format(value))


q = Manager().Queue()
print('start')
pool = Pool()
pool.apply(put, (q,))
pool.apply(get, (q,))
pool.close()
pool.join()
print('end')
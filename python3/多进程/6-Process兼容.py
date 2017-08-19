from multiprocessing import Process


def print_1():
    print('1')
P = Process(target=print_1)
P.start()
P.join()
print('main')

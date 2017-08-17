from threading import Thread
import time


def test():
    print('123')
    time.sleep(2)

# if __name__ == '__main__':
#     for i in range(5):
#         test()

for i in range(5):
    t = Thread(target= test)
    t.start()
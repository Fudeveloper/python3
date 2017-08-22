# 解决多线程（多进程）程序中，收集数据和处理数据的速度不同，找一个第三者（queue）来使生产者和消费者的不直接通信，降低它们的耦合性（解耦）
import queue
import threading
import time


class Producer(threading.Thread):
    def run(self):
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    queue.put('生产的产品{0}'.format(i))
                    print('生产产品{0}'.format(i))
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    msg = '{0}消费了{1}'.format(threading.current_thread(), queue.get())
                    print(msg)
            time.sleep(1)

queue = queue.Queue()
for i in range(500):
    queue.put('初始产品{0}'.format(i))

for i in range(2):
    p = Producer()
    p.start()

for i in range(5):
    c = Consumer()
    c.start()


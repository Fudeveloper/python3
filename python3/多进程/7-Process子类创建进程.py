from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self,sleep_time):
        super().__init__()
        self.sleep_time=sleep_time

    def run(self):
        print(self.sleep_time)


mp = MyProcess(5)
mp.start()



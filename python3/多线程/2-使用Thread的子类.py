from threading import Thread


class MyThread(Thread):
    def run(self):
        print(self.name)


for i in range(5):
   t = MyThread()
   t.start()
   #
   t.join()

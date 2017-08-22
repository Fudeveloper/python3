from multiprocessing import Process
def loop():
    while True:
        pass

p = Process(target=loop)
p.start()
loop()
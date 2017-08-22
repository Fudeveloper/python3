from threading import Thread
# 定义一个死循环方法
def loop():
    while True:
        pass
t = Thread(target=loop)
t.start()
while True:
    pass

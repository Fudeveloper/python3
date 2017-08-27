import asyncio
import threading
@asyncio.coroutine
def hello():
    print('hello world {0}'.format(threading.current_thread()))
    yield from asyncio.sleep(2)
    print('hello again {0}'.format(threading.current_thread()))

task = [hello(),hello()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))

'''
由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
'''
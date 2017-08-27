import time

def cosumer():
    print('jinru')
    r = ''
    while True:
        print('---1---')
        result = yield r
        print('---2---')
        time.sleep(1)
        if result == None:
            return
        print('消费者在消费{0}'.format(result))

        r = 'ok'
        print('---3---')


def producer(c):
    c.send(None)
    n = 0

    while n < 5:
        n += 1
        print('生产者在生产{0}'.format(n))

        what = c.send(n)
        print('消费者返回了{0}'.format(what))
    c.close()

c = cosumer()
producer(c)

'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

首先调用c.send(None)启动生成器；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
'''
def f1():
    while True:
        print('1')
        yield None


def f2():
    while True:
        print('2')
        yield None

t1 = f1()
t2 = f2()

while True:
    next(t1)
    next(t2)

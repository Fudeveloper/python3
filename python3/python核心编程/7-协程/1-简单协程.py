def start():
    print('10')
    yield 1
    print('20')
    yield 2
    print('30')
    yield 3

st = start()        # 协程最简单的风格-控制函数的阶段性执行
print(next(st))
print(next(st))
print(next(st))
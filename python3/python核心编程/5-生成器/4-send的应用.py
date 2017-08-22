def fib(num):
    a, b = 0,1
    for i in range(num):
        temp = yield b
        a, b = b, a+b

f = fib(5)
# f.send('hha ')
# TypeError: can't send non-None value to a just-started generator
# 第一次调用send时，程序不知道该将参数传递给谁

# f.send()
# TypeError: send() takes exactly one argument (0 given)

# 解决方案：第一次调用时，传递None
f.send(None)


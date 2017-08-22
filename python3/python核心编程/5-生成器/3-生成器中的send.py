def fib(num):
    a, b = 0, 1
    for i in range(num):
        temp = yield b  # 当调用send方法时，会将send方法中的参数当作整个表达式：yield b的值
        print(args)
        a, b = b, a+b

f = fib(5)
print(next(f))
print(next(f))
print(f.send('hha '))

# 1
# None
# 1
# hha
# 2


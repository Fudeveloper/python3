def fib(num):
    i = 0
    while i<5:
        if i == 0:
            temp = yield i
            print(temp)
        else:
            yield i
            print(temp)
        i += 1
        # a, b = b, a+b

f = fib(5)
print(f.send(None))
print(f.send('haha'))

# 此时，无论send任何值，都不会将temp的值刷新
print(f.send('ff'))
# 0
# haha
# 1
# haha
# 2
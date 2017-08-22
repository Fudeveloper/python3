def fib(num):
    a,b=0,1
    for i in range(num):
        yield b
        a,b=b,a+b



for i in fib(5):
    print(i)

# 1
# 1
# 2
# 3
# 5
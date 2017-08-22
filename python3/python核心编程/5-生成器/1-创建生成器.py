# a =(x*2 for x in range(20))
# print(a)        #<generator object <genexpr> at 0x7f67bd1be948>

def fib(num):
    a,b=0,1
    for i in range(num):
        print('--1--')
        yield b
        print('--2--')
        a,b=b,a+b
        print('--3--')

f = fib(5)
print(f)        #<generator object fib at 0x7fbe16f2f948>
print(next(f))
# --1--
# 1
# 发现打印--1--后，程序暂停，说明yield在返回一个值后，执行到下一次yield时暂停

print(next(f))
# --2--
# --3--
# --1--
# 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称为闭包
def test(number):
    print('1，初始化内部方法')

    def test_in(number_in):
        print('2')
        print(number+number_in)
    print('返回闭包结果')

    # 这里返回的就是闭包的结果
    return test_in

ret = test(100)
ret(1)
ret(200)
ret(300)

# 1
# 3
# 2
# 101
# 2
# 300
# 2
# 400

def test(a,b):
    def test_in(number_in):
        print(a*number_in+b)
    return test_in

line1 = test(1,2)
line1(3)        # 5

line2 = test(10,2)
line2(4)        # 42

line1(4)
# 6     # 函数line1依然存在，不会在执行一次后消亡，并且，闭包可以增加代码的复用率
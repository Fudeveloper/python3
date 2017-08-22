def decorate(func):
    def inner():
        print('--验证--')
        if False:
            func()
        else:
            print('--未通过--')
    return inner

@decorate
def f1():
    print('--f1--')

@decorate
def f2():
    print('--f2--')

f1()
f2()

# true状态下
# --验证--
# --f1--
# --验证--
# --f2--

# false状态下
# --验证--
# --未通过--
# --验证--
# --未通过--
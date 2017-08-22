def decorate(func):
    def wrapper():
        print('---装饰---')
        return_value = func()
        return return_value
    return wrapper

@decorate
def f1():
    print('--f1--')
    return 'haha'

ret = f1()
print('ret={0}'.format(ret))

# ---装饰---
# --f1--
# ret=haha
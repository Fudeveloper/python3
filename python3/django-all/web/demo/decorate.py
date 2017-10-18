# 装饰器

def decorate(func):
    def wrapper(*args,**kwargs):
        print('--装饰--')
        return_value = func(*args,**kwargs)
        return return_value
    return wrapper
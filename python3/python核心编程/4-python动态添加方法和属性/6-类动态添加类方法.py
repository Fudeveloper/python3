# 应用场景：在不改动已经写好的功能时，可以让程序发生适应性变化
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('{0}的eat方法'.format(self.name))


@classmethod
def print_num(self,num):
    print('num={0}'.format(num))

Person.print_num = print_num

Person.print_num(3)     #num=3


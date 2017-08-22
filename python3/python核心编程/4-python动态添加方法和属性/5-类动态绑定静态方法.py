class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('{0}的eat方法'.format(self.name))

    @staticmethod
    def sm1():
        print('sm1')

@staticmethod
def sm2():
    print('sm2')
Person.sm2 = sm2
Person.sm2()
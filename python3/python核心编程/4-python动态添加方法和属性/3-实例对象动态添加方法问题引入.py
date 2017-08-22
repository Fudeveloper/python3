from Person import Person
class Person1(Person):
    def __init__(self,name,age):
        super(Person1, self).__init__(name,age)

p1 = Person1('wang',30)
p1.eat()        #wang的eat方法


def run(self):
    print('{0}的fun方法'.format(self.name))
p1.run = run
p1.run() #虽然p1中 run属性已指向第10行方法，但是这句代码还不正确
        # 因为run属性指向的函数 是后来添加的，p1.run的时候，并没有把p1当做第          #一个参数，导致了第10行的函数调用的时候，出现缺少参数的问题
#TypeError: run() missing 1 required positional argument: 'self'
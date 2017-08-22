import types
from Person import Person

class Person1(Person):
    def __init__(self,name,age):
        super(Person1,self).__init__(name,age)

p1 = Person1('LIU',3)
def run(self):
    print('{0}的run方法'.format(self.name))

p1.run = types.MethodType(run, p1)
p1.run()
# LIU的run方法
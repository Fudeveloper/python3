class Student(object):
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        self.__age = new_age

std = Student(20)
print(std.age)      # 20

std.age = 50
print(std.age)      # 50
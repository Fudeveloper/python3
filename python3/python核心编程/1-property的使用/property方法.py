class Student(object):
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

    age = property(get_age, set_age)

std = Student(20)
print(std.age)

std.age = 50
print(std.age)
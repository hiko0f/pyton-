
class Parent:
    pass



class Child(Parent):
    pass


class Human:
    height = 180



class Student(Human):
    width = 30



class Worker(Human):
    salary = 100

jack = Student()

max = Worker()

# =-====================
class Shape:
    height = 15
    width = 20

class Rectangle(Shape):
    pass

class Rectangle(Rectangle):
    color = "Red"

class Car:
    name = "BMW"
    _name = "Toyota"
    __name = "Mazda"

    def __init__(self):
    self.module  = "E39"
    self._module = "Land Cruiser 200"
    self.__model = "RX8"


    def print_car(self):
        print(self.name)
        print(self._name)
        print(self.__name)
        print(self.model)
        print(self._model)
        print(self.__model)

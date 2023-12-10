print("============ Student ===============")


class Student:
    # конструктор класу Student
    def __init__(self, height=160, weight=60):
        self.height = height
        self.weight = weight
        print(self.height)
        print(self.weight)


first_student = Student()  # перший спосіб викликати студента
Student.__init__(self=first_student)  # другий спосіб викликати студента

print("height = ", first_student.height)  # третій спосіб викликати параметри студента
print("weight = ", first_student.weight)

second_student = Student(height=180, weight=85)  # тут викликається метод __init__

print("\nheight = ", second_student.height)
print("weight = ", second_student.weight)

print("============ Car ===============")


class Car:
    color = "red"
    vendor = "Ford"
    speed = 0

    def __init__(self, vendor, color):
        self.vendor = vendor
        self.color = color

    def drive(self, speed):
        if self.speed + speed < 200:
            self.speed += speed
        else:
            print("Ви перевищіли швидкість")


tesla = Car(vendor="Tesla", color="blue")

print("vendor = ", tesla.vendor)
print("color = ", tesla.color)
print("start speed = ", tesla.speed)
tesla.drive(100)
print("current speed = ", tesla.speed)
tesla.drive(50)
print("current speed = ", tesla.speed)
tesla.drive(100)
print("current speed = ", tesla.speed)
second_student
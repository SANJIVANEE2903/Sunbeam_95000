
class Person:

    def __init__(self, name = "", age = 0):
        self.__name = name
        self.__age = age

    def display_person(self):
        print(f"name : {self.__name}, age = {self.__age}")


class Student(Person):
    def __init__(self, name, age, rollno=0, marks=0.0):
        Person.__init__(self, name, age)
        self.__rollno = rollno
        self.__marks = marks

    def display_student(self):
        Person.display_person(self)
        print(f"rollno : {self.__rollno}, marks : {self.__marks}")

#p1 = Person("abc", 35)
#p1.display_person()

s1 = Student("abc", 16, 12, 98.0)
s1.display_student()


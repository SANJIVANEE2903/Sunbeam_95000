
class Student:
    def __init__(self, name=" ", rollno = 0, std = 0):
        self.__name = name
        self.__rollno = rollno
        self.__std = std

    def __str__(self):
        return f"name = {self.__name}, rollno = {self.__rollno}, std = {self.__std}"


class School:
    def __init__(self):
        self.__studlist = list()


    def add_student(self, name, rollno, std):
        s = Student(name, rollno, std)
        self.__studlist.append(s)

    def display_students(self):
        for s in self.__studlist:
            print(s)


sch = School()

sch.add_student("abc", 12, 4)
sch.add_student("xyz", 14, 5)

sch.display_students()
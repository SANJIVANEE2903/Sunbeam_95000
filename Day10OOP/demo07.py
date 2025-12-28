
# Multi-level Inheritance

class Person:
    def __init__(self, name=" ", age=1):
        self.__name = name
        self.__age = age
    
    def display_person(self):
        print(f"Person: name={self.__name}, age={self.__age}")

# Emp is a Person
class Emp(Person):
    def __init__(self, name=" ", age=1, id=1, sal=0.0):
        Person.__init__(self, name, age) # call Person's initializer
        self.__id = id
        self.__sal = sal

    def display_emp(self):
        Person.display_person(self)
        print(f"Emp: id={self.__id}, sal={self.__sal}")    

# Manager is a Emp
class Manager(Emp):
    def __init__(self, name=" ", age=1, id=1, sal=0, team=1):
        Emp.__init__(self, name, age, id, sal)
        self.__team = team

    def display_manager(self):
        Emp.display_emp(self)
        print(f"Manager: team={self.__team}")

# Manager obj
m1=Manager("Sameer", 44, 12, 50000.0, 20)
m1.display_manager()

print("Manager MRO: ", Manager.mro())
    # Manager, Emp, Person, Object
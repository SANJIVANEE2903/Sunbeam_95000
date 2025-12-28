
#   attr    :   public
#   _attr   :   protected
#   __attr  :   private

# internally attribute name is prefixed with _ClassName__attr

class Person:
    def __init__(self, name = "", age = 0, addr = ""):
        self.__name = name
        self.__age = age
        self.__address = addr

    def display(self):
        print(f"name : {self.__name}, age : {self.__age}, address : {self.__address}")

    def set_name(self, name):
        # add validation
        self.__name = name

    def set_age(self, age):
        # add validation
        self.__age = age

    def set_address(self, address):
        # add validation
        self.__address = address

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

p1 = Person("abc", 35, "pune")
p1.__address = "mumbai"     # address will not be changed
p1.display()

print("After updating address : ")
p1.set_address("mumbai")
p1.display()
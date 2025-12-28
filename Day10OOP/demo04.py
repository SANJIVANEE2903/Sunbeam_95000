class Person:
    #initilizer
    def __init__(self, name ="", age =0, addr = ""):
        self.name = name
        self.age = age
        self.address = addr


    #de initilizer
    def __del__(self):
        print("Person object is destroyed")

     # facilitator
    def display(self):
        print(f"person : name = {self.name}, age = {self.age}, address = {self.address}")

    def canVote(self):
        if(self.age >= 18):
            print(f"{self.name} person can vote")
        else:
            print(f"{self.name} person can not vote")


p1 = Person("abc", 34, "pune")
p1.mobile = "1234567890"
print(f"p1 attrs : {p1.__dict__}")
p1.display()
p1.canVote()

p2 = Person()
p2.email = "test@gmail.com"
p2.age = 17
print(f"p2 attrs : {p2.__dict__}")
p2.display()
p2.canVote()  
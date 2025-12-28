
class Person:
    pass

p1 = Person()
p1.name = "abc"
p1.age = 34
p1.address = "pune"

print(f"type(p1) : {type(p1)}")
print(f"p1 attrs : {p1.__dict__}") # {'name': 'abc', 'age': 34, 'address': 'pune'}

p2 = Person()
p2.name =  "xyz"
p2.age = 40
p2.mobile =  "1234567890"

print(f"type(p2) : {type(p2)}")
print(f"p2 attrs : {p2.__dict__}") # {'name': 'xyz', 'age': 40, 'mobile': '1234567890'}

print(f"name of p1 =", p1.name)
print(f"addr of p1 =", p1.address)

print(f"name of p2 =", p2.name)
print(f"mobile of p2 =", p2.mobile)
class Person:
    pass

p1 = Person()
setattr(p1, "name", "abc")
setattr(p1, "age", 34)
setattr(p1, "address", "pune")

print(f"type(p1) : {type(p1)}")
print(f"p1 attrs : {p1.__dict__}") # {'name': 'abc', 'age': 34, 'address': 'pune'}



p2 = Person()
setattr(p2, "name", "abc")
setattr(p2, "age", 34)
setattr(p2, "address", "pune")

print(f"type(p2) : {type(p2)}")
print(f"p2 attrs : {p2.__dict__}") # {'name': 'xyz', 'age': 40, 'mobile': '1234567890'}


print(f"name of p1 =" + getattr(p1, "name"))
print(f"addr of p1 =" + getattr(p1, "address"))

print(f"name of p2 =" + getattr(p2, "name"))
print(f"mobile of p2 =" + getattr(p2, "mobile"))
import abc

class Shape(abc.ABC):
    # ...
    @abc.abstractmethod
    def calcarea(self):
        pass

class Rectangle(Shape):
    def __init__(self, len=0, br=0):
        self.length = len
        self.breadth = br
    
    def calcarea(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, rad):
        self.radius = rad
    
    def calcarea(self):
        return 3.142 * self.radius * self.radius

r = Rectangle(10, 8)
print("rect area:", r.calcarea())

c = Circle(7)
print("circle area:", c.calcarea())
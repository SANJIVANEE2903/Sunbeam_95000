
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    def display(self):
        print(f"x = {self.__x}, y = {self.__y}")

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

p1 = Point(1, 1)
p1.display()

p2 = Point(1, 1)
p2.display()

p = p1 + p2
p.display()

print(f"p1 == p2 : {p1 == p2}")

print(p1)
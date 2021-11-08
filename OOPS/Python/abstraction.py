from abc import ABC
class Shape(ABC):
    def area(self):
        pass
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
if __name__=="__init__":
    square = Square(10)
    print(square.area())
    print(square.perimeter())
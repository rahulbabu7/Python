from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        pass
    def circum(self):
        pass

class triangle(Shape):
    def area(self):
        print(3.14 *2*2)
    def circum(self):
        print( 2 *3.14)

triang = triangle()
triang.area()
triang.circum()
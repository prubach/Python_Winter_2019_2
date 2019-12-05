import math

from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, a=8, b=9):
        self.set_params(a, b)

    @abstractmethod
    def calc_surface(self):
        pass

    def set_params(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self._b) + "] at " + str(hex(id(self)))

class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self._b

class Circle(Shape):
    def __init__(self, a):
        # call constructor from super class (Shape)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi*self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

# not possible because it is an abstract class
#s = Shape(45, 56)
r1 = Rectangle(4, 6)
print(r1)
print(r1.calc_surface())
c1 = Circle(5)
print(c1)
#print(c1.calc_surface())


# print(r1.calc_surface())
# print(r1.get_a())
# print(r1.get_b())
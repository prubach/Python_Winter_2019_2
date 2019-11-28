class Rectangle:
    def __init__(self, a=8, b=9):
        self.set_params(a, b)

    def set_params(self, a, b):
        self.__a = a
        self.__b = b

    def calc_surface(self):
        return self.__a*self.__b

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.__b) + "] at " + str(hex(id(self)))

r1 = Rectangle(4, 6)
r1.__a = 10
r1.a = 20
print(r1)
print(r1.calc_surface())
print(r1.get_a())
print(r1.get_b())
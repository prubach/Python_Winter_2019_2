class Rectangle:
    def __init__(self, a=8, b=9):
        self.set_params(a, b)
        #self.a = a
        #self.b = b

    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b

    @staticmethod
    def calculate_surface(aa, bb):
        return aa*bb

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

print(Rectangle.calculate_surface(7, 10))

r1 = Rectangle(a=5)
r1.b = 10
r1.c = 55
print(r1.calc_surface())
print(r1.c)
#print(Rectangle.calculate_surface(7, 10))
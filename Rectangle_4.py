class Rectangle:
    def __init__(self, a=8, b=9):
        self.set_params(a, b)

    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

    def __str__(self):
        return "Rect: {0} by {1}".format(self.a, self.b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Rectangle(a, b)

    def __lt__(self, other):
        self_area = self.calc_surface()
        other_area = other.calc_surface()
        return self_area < other_area


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 5)
r3 = Rectangle(1, 2)
r = r1 + r2 + r3
print(r.calc_surface())

print(r1<r2)

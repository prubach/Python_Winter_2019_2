class Rectangle:
    num_rect = 0

    def __init__(self, a=8, b=9):
        self.set_params(a, b)
        Rectangle.num_rect+=1

    def __del__(self):
        Rectangle.num_rect-=1
        print(self.__class__.__name__ + " destroyed")

    @classmethod
    def how_many(cls):
        print("We have {0} rectangles".format(Rectangle.num_rect))

    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

    def __str__(self):
        return "Rect: {0} by {1}".format(self.a, self.b)

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 5)
r3 = Rectangle(1, 2)
r1.how_many()
r3.how_many()
del r3
r2.how_many()
class Rectangle:
    def set_params(self, a, b):
        self.a = a
        self.b = b
    def calc_surface(self):
        return self.a*self.b

r = Rectangle()
r.set_params(5, 6)
print(r.calc_surface())
r2 = Rectangle()
r2.set_params(23, 2)
print(r2.calc_surface())

class Rectangle:
    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle()
r.set_params(5, 6)
print(r.calc_surface())
r2 = Rectangle()
r2.set_params(23, 2)
print(r2.calc_surface())

r3 = Rectangle()
r3.set_params(7, 9)
print()

r4 = r3
x = [r, r2, r3, r4]
print('before: ')
print(x)
# 2 pointers to the same list
#y = x
z = x
# copy pointers but not objects
#y = x.copy()
from copy import deepcopy
y = deepcopy(x)

print(y)
y[1].set_params(99, 8)
y[2].set_params(88, 3)
print('after:')
print(x)
print(y)
print(z)


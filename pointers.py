a = 5
b = a
b = 6
print('a=' + str(a))
print('b=' + str(b))
s1 = 'Hello'
s2 = s1
x = [a, b, s1, s2]
# 2 pointers to the same list
y = x
z = x.copy()
y[1] = 8
y[2] = 'World'
print(x)
print(y)
print(z)






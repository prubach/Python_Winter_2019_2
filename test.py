d = {'k1': 'Hello', 'k2': "World" }
print(d['k1'] + " " + d['k2'])
print(d.get('k1'))
d['k2'] = 'Everyone'
d['k3'] = 'Python'
print()
for i in d.keys():
    print(d.get(i))

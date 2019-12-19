a = 10
b = 20
try:
    e = str(d)
    c = a*d
    if b>a:
        raise Exception("Error: b>a")
    print("continuing in try except")
except Exception as e:
    print('exception occurred: ' + str(e))
print("continuing...")

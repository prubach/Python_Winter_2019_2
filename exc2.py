while True:
    try:
        x = int(input('Please enter x: '))
        break
    except (KeyboardInterrupt, ValueError):
        print('Please try again')
print("I got x: " + str(x))
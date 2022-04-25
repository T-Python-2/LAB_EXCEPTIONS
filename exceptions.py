#Exceptions lab

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError:
    print("Incorrect variable is used in the addition operation.")
else:
    print("The operation is successfully done!")

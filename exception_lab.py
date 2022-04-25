#- Find what type of exception is raised.
"""def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    print(additoin(10, 20))
except Exception as e:
    print(e.__class__)
else:
    print("operation is successful")
"""


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    print(additoin(10, 20))
except NameError as ne:
    print(f"facing problem with a variable it's {ne}")    
else:
    print("the operation is successful")


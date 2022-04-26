
def additoin(x, y):
    x = 10
    y = 20
   
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as ne:
   print( "worng parameter assignment!!", ne)
else:
    print("the operation is successful")
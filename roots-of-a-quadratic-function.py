import math

a = int(input('Type your "a" value: '))
b = int(input('Type your "b" value: '))
c = int(input('Type your "c" value: '))

discrim = b**2-4*a*c

if discrim < 0:
    print("This equation has no real solution")
elif discrim == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print("This equation has no real solution")
else:
    firstx = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    secondx = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print("This equation has two solutions: ", firstx, " or", secondx)
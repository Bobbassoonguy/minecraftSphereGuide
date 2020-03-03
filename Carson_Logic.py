import math
import random


def f(x):
    if(x == -1):
        return 0
    return x


def circle(radius):
    print(radius)
    array = [[0 for i in range(2*radius)] for j in range(2*radius)]
    r2 = radius**2
    for z in range(0, math.ceil(radius)):
        z2 = z**2
        dist = r2-z2
        x2 = dist
        x = math.sqrt(x2)
        print((radius-0.5)**2)
        print((radius+0.5)**2)
        for n in range(math.floor(x)-1, math.floor(x) + 2):
            print(str(z) + ", " + str(n) + ", " + str(z**2+n**2))
            if z**2+n**2 > (radius-0.5)**2 and z2 + n**2 <= (radius+0.5)**2:
                print("yes")
                for s in range(-1, 2, 2):
                    for t in range(-1, 2, 2):
                        array[n*s+math.floor(radius-f(s))][z*t+math.floor(radius-f(t))] = 1
                        array[z*t+math.floor(radius-f(t))][n*s+math.floor(radius-f(s))] = 1
    for row in array:
        print(row)


circle(5)

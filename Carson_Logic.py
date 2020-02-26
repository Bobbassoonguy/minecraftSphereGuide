import math
import random


def circle(radius):
    print(radius)
    r2 = radius**2
    array = [[]]
    for x in range(0, 2*radius):
        for z in range(0, 2*radius):
            array[x][z] = 0
    for z in range(0, radius):
        z2 = z**2
        dist = r2-z2
        x2 = dist
        x = math.sqrt(x2)


print("Do the thing")
circle(5)

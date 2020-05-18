import math
import random


def f(x):
    if x == -1:
        return 0
    return x


def circle(radius):
    # print(radius)
    array = [[0 for i in range(2*radius)] for j in range(2*radius)]
    r2 = radius**2
    for z in range(0, math.ceil(radius)):
        z2 = z**2
        dist = r2-z2
        x2 = dist
        x = math.sqrt(x2)
        # print((radius-0.5)**2)
        # print((radius+0.5)**2)
        for n in range(math.floor(x)-1, math.floor(x) + 2):
            # print(str(z) + ", " + str(n) + ", " + str(z**2+n**2))
            if z**2+n**2 > (radius-0.5)**2 and z2 + n**2 <= (radius+0.5)**2:
                # print("yes")
                for s in range(-1, 2, 2):
                    for t in range(-1, 2, 2):
                        array[n*s+math.floor(radius-f(s))][z*t+math.floor(radius-f(t))] = 1
                        array[z*t+math.floor(radius-f(t))][n*s+math.floor(radius-f(s))] = 1
    # for Row in array:
        # print(Row)
    c = []
    for a in range(2*radius):
        for b in range(2*radius):
            if array[a][b] == 1:
                c.append([a, b])
    return c


def sphere(radius):
    # print(radius)
    array = [[[0 for i in range(2 * radius)] for j in range(2 * radius)] for k in range(2 * radius)]
    r2 = radius ** 2
    for z in range(0, math.ceil(radius)):
        z2 = z ** 2
        dist = r2 - z2
        for y in range(0, math.ceil(math.sqrt(dist))):
            y2 = y ** 2
            x2 = dist - y2
            x = math.sqrt(x2)
            # print((radius-0.5)**2)
            # print((radius+0.5)**2)
            for n in range(math.floor(x) - 1, math.floor(x) + 2):
                n2 = n ** 2
                # print(str(z) + ", " + str(n) + ", " + str(z**2+n**2))
                if (radius - 0.5) ** 2 < z2 + y2 + n2 <= (radius + 0.5) ** 2:
                    # print("yes")
                    for s in range(-1, 2, 2):
                        for t in range(-1, 2, 2):
                            for u in range(-1, 2, 2):
                                array[y * u + math.floor(radius - f(u))][n * s + math.floor(radius - f(s))][z * t + math.floor(radius - f(t))] = 1
                                array[y * u + math.floor(radius - f(u))][z * t + math.floor(radius - f(t))][n * s + math.floor(radius - f(s))] = 1
                                array[n * s + math.floor(radius - f(s))][y * u + math.floor(radius - f(u))][z * t + math.floor(radius - f(t))] = 1
                                array[z * t + math.floor(radius - f(t))][y * u + math.floor(radius - f(u))][n * s + math.floor(radius - f(s))] = 1
                                array[n * s + math.floor(radius - f(s))][z * t + math.floor(radius - f(t))][y * u + math.floor(radius - f(u))] = 1
                                array[z * t + math.floor(radius - f(t))][n * s + math.floor(radius - f(s))][y * u + math.floor(radius - f(u))] = 1
    # for Row in array:
        # print(Row)
    c = []
    for a in range(2 * radius):
        for b in range(2 * radius):
            for d in range(2 * radius):
                if array[a][b][d] == 1:
                    c.append([a, b, d])
    return c

def sphereFormatted(radius):
    arrayOfCoords = sphere(radius)
    array = [[]]

    for triplet in arrayOfCoords:
        if triplet[0] == len(array):
            array.append([])
        array[len(array) - 1].append(triplet)
    for layer in range(0, len(array)):
        # arrayOfCoords = circle(radius) # CARSON - put your array of coordinate pairs here
        # arrayOfCoords = sphere(radius)
        for a in array[layer]:
            # print(arrayOfCoords[layer])
            a[0] = a[0] - radius
            a[1] = a[1] - radius
            a[2] = a[2] - radius
            temp = a[0]
            a[0] = a[2]
            a[2] = temp
    for layer in range(len(array) - 1, -1, -1):
        if array[layer][0][2] < 0:
            array.pop(layer)

    return array


list1 = sphere(10)
# for row in list1:
    # print(row)

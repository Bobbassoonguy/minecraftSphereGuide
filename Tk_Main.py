from tkinter import *
import tk_canvasFrame_V2 as canvFrame
import tk_parameterFrame as pFrame
from Carson_Logic import circle
from Carson_Logic import sphere
import random
import colorsys

LABEL_FONT = ("Times","30","bold")
BUTTON_FONT = ("Times","15")

rainbowList = []

def RGB(red,green,blue): return '#%02x%02x%02x' % (red,green,blue)


#root application, can only have one of these.
root = Tk()


root.title("Sphere Calculator")

labelText = "Sphere Calculator"
if random.randint(0,200) == 0:
    labelText = "MINCERAFT Sphere Calculator"

topLabel = Label(root, text=labelText, font=LABEL_FONT)
topLabel.grid(row=0)

canv = canvFrame.SquareDispCanvas(root)

radius = 20
for hue in range(0,1000,int(1000/(radius))):
    (r, g, b) = colorsys.hsv_to_rgb(hue/1000, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    rainbowList.append(RGB(R,G,B))

arrayOfCoords = sphere(radius)
array = [[]]
canv.gridSize = [2*radius,2*radius]
for triplet in arrayOfCoords:
    if triplet[0] == len(array):
        array.append([])
    array[len(array)-1].append(triplet)
for layer in range(0,len(array)):
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
for layer in range(len(array)-1, -1, -1):
    if array[layer][0][2] < 0:
        array.pop(layer)

for layer in range(0, len(array)):
    canv.drawTheseRectangles(array[layer],color=rainbowList[layer])

canv.drawCanvasGrid()

parameterFrame = pFrame.parameterFrame(root)



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
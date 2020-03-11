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

maxRad = 10

for hue in range(0,100,int(100/maxRad)):
    (r, g, b) = colorsys.hsv_to_rgb(hue/100, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    rainbowList.append(RGB(R,G,B))

for radius in range(1,maxRad):
    arrayOfCoords = circle(radius) # CARSON - put your array of coordinate pairs here
    for a in arrayOfCoords:
        a[0] = a[0]-radius
        a[1] = a[1]-radius

    canv.drawTheseRectangles(arrayOfCoords,color=rainbowList[radius])

canv.drawCanvasGrid()

parameterFrame = pFrame.parameterFrame(root)



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
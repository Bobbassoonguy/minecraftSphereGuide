from tkinter import *
import tk_canvasFrame_V2 as canvFrame
import tk_parameterFrame as pFrame
from Carson_Logic import circle
import random

LABEL_FONT = ("Times","30","bold")
BUTTON_FONT = ("Times","15")

#root application, can only have one of these.
root = Tk()


root.title("Sphere Calculator")

labelText = "Sphere Calculator"
if random.randint(0,200) == 0:
    labelText = "MINCERAFT Sphere Calculator"

topLabel = Label(root, text=labelText, font=LABEL_FONT)
topLabel.grid(row=0)

canv = canvFrame.SquareDispCanvas(root)
parameterFrame = pFrame.parameterFrame(root)

radius = 10
arrayOfCoords = circle(radius) # CARSON - put your array of coordinate pairs here
for a in arrayOfCoords:
    a[0] = a[0]-radius
    a[1] = a[1]-radius

canv.drawTheseRectangles(arrayOfCoords)



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
from tkinter import *
import tk_canvasFrame_V2 as canvFrame
import tk_parameterFrame as pFrame
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

arrayOfCoords = [] # CARSON - put your array of coordinate pairs here

canv.drawTheseRectangles(arrayOfCoords)



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
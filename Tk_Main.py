from tkinter import *
import tk_canvasFrame_V2 as canvFrame
import tk_parameterFrame as pFrame
from Carson_Logic import circle
from Carson_Logic import sphereFormatted
import random


LABEL_FONT = ("Times","30","bold")
SUBLABEL_FONT = ("Times","12")
BUTTON_FONT = ("Times","15")


class parameterFrame:
    def __init__(self, master=None, defaultR=20):
        self.master = master
        self.defaultR = defaultR

        # Create display frame
        self.frame = Frame(self.master, bg="red")
        self.frame.grid(row=1, sticky=NSEW) # TODO move this out of class

        self.rframe()
        self.lframe()

    def linkToCanvas(self, canv):
        self.canvFrame = canv

    def rframe(self):
        self.radiusFrame = Frame(self.frame, bg="blue") # TODO Remove background
        self.radiusFrame.grid(column=0,row=0, sticky=NW)  # TODO move this out of class

        radiusEntryLabel = Label(self.radiusFrame, text="Radius:", font=SUBLABEL_FONT)
        radiusEntryLabel.grid(row=0, sticky=W)

        self.radiusEntry = Entry(self.radiusFrame,width=7)
        self.radiusEntry.grid(row=1,sticky=W)
        self.radiusEntry.insert(0, str(self.defaultR))

        self.radiusUpdateButton = Button(self.radiusFrame,text="Update",command=updateRad)
        self.radiusUpdateButton.grid(row=1,column=1,sticky=W)

    def lframe(self):
        self.layerFrame = Frame(self.frame, bg="yellow")  # TODO Remove background
        self.layerFrame.grid(column=1,row=0, sticky=N)  # TODO move this out of class

        layerEntryLabel = Label(self.layerFrame, text="Layer:", font=SUBLABEL_FONT)
        layerEntryLabel.grid(row=0, sticky=W)

        self.layerEntry = Entry(self.layerFrame, width=7)
        self.layerEntry.grid(row=1, sticky=W)
        self.layerEntry.insert(0, "0")

        self.layerUpdateButton = Button(self.layerFrame, text="Update", command=dispLayer)
        self.layerUpdateButton.grid(row=1, column=1, sticky=W)

    def getR(self):
        rad = int(self.radiusEntry.get())
        if type(rad) is not int and type(rad) is not float:
            return None
        else:
            return rad

    def getL(self):
        layer = int(self.layerEntry.get())
        if type(layer) is not int:
            return None
        else:
            return layer




def createTitle():
    labelText = "Sphere Calculator"
    if random.randint(0, 200) == 0:
        labelText = "MINCERAFT Sphere Calculator"
    topLabel = Label(root, text=labelText, font=LABEL_FONT)
    topLabel.grid(row=0)

def updateRad():
    newRadius = pFrame.getR()
    if newRadius is not None:
        print("Radius Updated")
        canv.updateRadius(newRadius)

def dispLayer():
    newLayer = pFrame.getL()
    if newLayer is not None:
        print("Layer Updated")
        canv.removeRectangles()
        canv.drawTheseRectangles(sphere[newLayer])


#root application, can only have one of these.
root = Tk()
root.title("Sphere Calculator")

createTitle()

radius = 64
Layer = 0

pFrame = parameterFrame(defaultR=radius)
canv = canvFrame.SquareDispCanvas(root, radius)
updateRad()

sphere = sphereFormatted(radius)

dispLayer()



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
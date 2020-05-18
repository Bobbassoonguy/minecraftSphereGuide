from tkinter import *
import tk_canvasFrame_V2 as canvFrame
import tk_parameterFrame as pFrame
from Carson_Logic import circle
from Carson_Logic import sphereFormatted
import math
import random


LABEL_FONT = ("Times","30","bold")
SUBLABEL_FONT = ("Times","12")
BUTTON_FONT = ("Times","10")


class parameterFrame:
    def __init__(self, master=None, defaultR=20):
        self.master = master
        self.defaultR = defaultR

        # Create display frame
        self.frame = Frame(self.master)
        self.frame.grid(row=1, sticky=NSEW) # TODO move this out of class

        self.rframe()
        self.lframe()
        self.rotFrame()
        self.adjFrame()

    def linkToCanvas(self, canv):
        self.canvFrame = canv

    def rframe(self):
        self.radiusFrame = Frame(self.frame, relief=RIDGE, bd=4)
        self.radiusFrame.grid(column=0,row=0, sticky=NW)  # TODO move this out of class

        radiusEntryLabel = Label(self.radiusFrame, text="Radius:", font=SUBLABEL_FONT)
        radiusEntryLabel.grid(row=0, sticky=W)

        self.radiusEntry = Entry(self.radiusFrame,width=7)
        self.radiusEntry.grid(row=1,sticky=W)
        self.radiusEntry.insert(0, str(self.defaultR))

        self.radiusUpdateButton = Button(self.radiusFrame,text="Update",command=updateRad)
        self.radiusUpdateButton.grid(row=1,column=1,sticky=W)

    def lframe(self):
        self.layerFrame = Frame(self.frame, relief=RIDGE, bd=4)
        self.layerFrame.grid(column=1,row=0, sticky=N)  # TODO move this out of class

        layerEntryLabel = Label(self.layerFrame, text="Layer:", font=SUBLABEL_FONT)
        layerEntryLabel.grid(row=0, sticky=W)

        self.layerAddButton = Button(self.layerFrame, text="  +  ", command=self.add1L)
        self.layerAddButton.grid(row=0, column=1, sticky=EW)

        self.layerSubtractButton = Button(self.layerFrame, text="  -  ", command=self.sub1L)
        self.layerSubtractButton.grid(row=0, column=2, sticky=EW)

        self.layerEntry = Entry(self.layerFrame, width=7)
        self.layerEntry.grid(row=1, sticky=W)
        self.layerEntry.insert(0, "1")

        self.layerUpdateButton = Button(self.layerFrame, text="Update", command=dispLayer)
        self.layerUpdateButton.grid(row=1, column=1, columnspan=2, sticky=W)

    def rotFrame(self):
        self.rotateFrame = Frame(self.frame, relief=RIDGE, bd=4)
        self.rotateFrame.grid(column=2, row=0, sticky=N)  # TODO move this out of class

        rotLabel = Label(self.rotateFrame, text="Rotate Display", font=SUBLABEL_FONT)
        rotLabel.grid(row=0, sticky=W, columnspan=2)

        self.CCWButton = Button(self.rotateFrame, text=" ↶ ", command=rotateCCW, font=BUTTON_FONT)
        self.CCWButton.grid(row=1, column=0, sticky=EW)

        self.CWButton = Button(self.rotateFrame, text=" ↷ ", command=rotateCW, font=BUTTON_FONT)
        self.CWButton.grid(row=1, column=1, sticky=EW)

    def adjFrame(self):
        self.adjacentLayerFrame = Frame(self.frame, relief=RIDGE, bd=4)
        self.adjacentLayerFrame.grid(column=3, row=0, sticky=N)  # TODO move this out of class

        self.aboveCheck = Checkbutton(self.adjacentLayerFrame, text="View Layer Above", command=toggleAbove, font=BUTTON_FONT, fg="blue")
        self.aboveCheck.grid(row=1, column=0, sticky=EW)

        self.belowCheck = Checkbutton(self.adjacentLayerFrame, text="View Layer Below", command=toggleBelow, font=BUTTON_FONT,fg="green")
        self.belowCheck.grid(row=2, column=0, sticky=EW)

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

    def add1L(self):
        currentLayer = self.getL()
        currentRadius = self.getR()
        if currentLayer is not None and currentRadius is not None:
            if currentLayer < -1:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(1+int(currentLayer)))
                dispLayer()
            elif currentLayer == -1:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(1))
                dispLayer()
            elif currentLayer < currentRadius:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(1+int(currentLayer)))
                dispLayer()

    def sub1L(self):
        currentLayer = self.getL()
        currentRadius = self.getR()
        if currentLayer is not None and currentRadius is not None:
            if currentLayer > 1:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(int(currentLayer)-1))
                dispLayer()
            elif currentLayer == 1:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(-1))
                dispLayer()
            elif currentLayer > -1*currentRadius:
                self.layerEntry.delete(0, len(self.layerEntry.get()))
                self.layerEntry.insert(0, str(int(currentLayer-1)))
                dispLayer()



aboveDisp = False
belowDisp = False



def createTitle():
    labelText = "Sphere Calculator"
    if random.randint(0, 200) == 0:
        labelText = "MINCERAFT Sphere Calculator"
    topLabel = Label(root, text=labelText, font=LABEL_FONT)
    topLabel.grid(row=0)

def updateRad():
    global radius
    newRadius = pFrame.getR()
    if newRadius is not None:
        print("Radius Updated")
        radius = newRadius

        global sphere
        sphere = sphereFormatted(radius)

        canv.updateRadius(radius)
        dispLayer()

def dispLayer():
    newLayer = pFrame.getL()
    if newLayer is not None:
        if newLayer == 0:
            newLayer = 1
        print("Layer Updated")
        canv.removeRectangles()
        newLayer -= (int)(newLayer/abs(newLayer))
        newLayer = abs(newLayer)
        canv.drawTheseRectangles(sphere[newLayer])
        if newLayer != -1*radius and belowDisp:
            layer2 = newLayer-1
            layer2 = abs(layer2)
            canv.drawTheseRectangles(sphere[layer2], "green")
        if newLayer != radius and aboveDisp:
            layer3 = newLayer+1
            layer3 = abs(layer3)
            canv.drawTheseRectangles(sphere[layer3], "blue")

def rotateCW():
    print("Rotated CW")
    origin = canv.originLoc
    if origin == "SW":
        canv.originLoc = "NW"
    elif origin == "NW":
        canv.originLoc = "NE"
    elif origin == "NE":
        canv.originLoc = "SE"
    elif origin == "SE":
        canv.originLoc = "SW"

    updateRad()
    dispLayer()

def rotateCCW():
    print("Rotated CCW")
    origin = canv.originLoc
    if origin == "NW":
        canv.originLoc = "SW"
    elif origin == "NE":
        canv.originLoc = "NW"
    elif origin == "SE":
        canv.originLoc = "NE"
    elif origin == "SW":
        canv.originLoc = "SE"

    updateRad()
    dispLayer()

def toggleAbove():
    global aboveDisp
    if aboveDisp:
        aboveDisp = False
    else:
        aboveDisp = True

    dispLayer()

def toggleBelow():
    global belowDisp
    if belowDisp:
        belowDisp = False
    else:
        belowDisp = True

    dispLayer()

#root application, can only have one of these.
root = Tk()
root.title("Sphere Calculator")

createTitle()

radius = 32
Layer = 1



pFrame = parameterFrame(defaultR=radius)
canv = canvFrame.SquareDispCanvas(root, radius)
updateRad()



#lifts window to top, but not permanently
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()
from tkinter import *
import tk_canvasFrame_V2 as canvFrame

LABEL_FONT = ("Times","15","bold")
BUTTON_FONT = ("Times","15")



class parameterFrame:
    def __init__(self, master=None):
        self.master = master
        self.canvFrame = None

        # Create display frame
        self.frame = Frame(self.master, bg="red")
        self.frame.grid(row=1, sticky=NSEW) # TODO move this out of class

        self.rframe()

    def linkToCanvas(self, canv):
        self.canvFrame = canv

    def updateCanvas(self):
        print("Update?")
        if type(self.canvFrame) != None:
            self.canvFrame.updateRadius()

    def rframe(self):
        self.radiusFrame = Frame(self.frame, bg="blue")
        self.radiusFrame.grid(column=0, sticky=W)  # TODO move this out of class

        radiusEntryLabel = Label(self.radiusFrame, text="Radius:", font=LABEL_FONT)
        radiusEntryLabel.grid(row=0, sticky=W)

        self.radiusEntry = Entry(self.radiusFrame)
        self.radiusEntry.grid(row=1,sticky=W)
        self.radiusEntry.insert(0, "10")

        self.radiusUpdateButton = Button(self.radiusFrame,text="Update",command=self.updateCanvas)
        self.radiusUpdateButton.grid(row=1,column=1,sticky=W)

    def getR(self):
        return self.radiusEntry.get()



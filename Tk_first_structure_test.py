from tkinter import *
import random


LABEL_FONT = ("Times","30","bold")
BUTTON_FONT = ("Times","15")

## This commit is from my laptop

##alex is a potato


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # self.gridSize = [258,258] # number of squares in the grid
        self.gridSize = [72, 72]  # number of squares in the grid

        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title
        self.master.title("MINECRAFT SPHERE CALCULATOR")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #Label

        labelText = "Sphere Calculator"
        if random.randint(0,200) == 0:
            labelText = "MINCERAFT Sphere Calculator"

        topLabel = Label(self, text=labelText, font=LABEL_FONT)
        topLabel.grid(row=0)

        self.canvasWidth = 0
        self.canvasHeight = 0
        self.canvasZoom = 20

        # self.bind("<Configure>", self.resizeCanvas)

        self.drawCanvasFrame()
        self.createBlankCanvas()
        self.canvas.bind("<MouseWheel>", self.mouseWheel)

        self.canvasScrolling()
        self.canvasZoomButtons()

        self.drawCanvasAxes()
        self.drawCanvasGrid()



    def createBlankCanvas(self):

        self.canvasZoom = 12

        self.canvasWidth = (self.canvasZoom * self.gridSize[0])
        self.canvasHeight = (self.canvasZoom * self.gridSize[1])


        self.canvas = Canvas(self.canvasFrame, width=self.canvasWidth, height=self.canvasHeight, bg='white')
        self.canvas.grid(row=0, column=0)

        # set the canvas as the size priority in the canvasFrame
        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.rowconfigure(0, weight=1)

    def drawCanvasFrame(self):
        self.canvasFrame = Frame(self, bd=10, relief=SUNKEN,bg="blue")
        self.canvasFrame.grid(row=2,sticky=NSEW)

        # give priority to the size of canvasFrame in root grid
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

    def mouseWheel(self, event):
        scroll = event.delta
        if abs(scroll) > 100:
            scroll = -1 * int(scroll / 120)

        self.canvas.yview(SCROLL, scroll, UNITS)

    def resizeCanvas(self, event):
        self.windowWidth = event.width - 70
        if abs(self.windowWidth - self.canvasWidth) > 20: ## re-draw the canvas if there are these many pixels of room
            self.canvasZoom = round(self.windowWidth / self.gridSize[0])

            self.updateCanvasSize()

    def updateCanvasSize(self):
        self.canvasWidth = (self.canvasZoom * self.gridSize[0])
        self.canvasHeight = (self.canvasZoom * self.gridSize[1])
        self.canvas.configure(width=self.canvasWidth, height=self.canvasHeight)
        for i in self.canvas.find_all():
            self.canvas.delete(i)
        self.canvasScrolling()
        self.drawCanvasAxes()
        self.drawCanvasGrid()

    def canvasScrolling(self):
        self.scroll_x = Scrollbar(self.canvasFrame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky=EW)
        self.scroll_y = Scrollbar(self.canvasFrame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        self.canvas.configure(scrollregion=(0, 0, self.canvasWidth,self.canvasHeight))
        self.canvas.grid()

    def canvasZoomButtons(self): #TODO "fill" frame button
        self.canvasZoomButtonFrame = Frame(self.canvasFrame)
        self.canvasZoomButtonFrame.grid(column=2, row=0, sticky=N)
        self.zoomInButton = Button(self.canvasZoomButtonFrame,text="+", width=3, font=BUTTON_FONT, command=self.zoomIn)
        self.zoomOutButton = Button(self.canvasZoomButtonFrame, text="-", width=3, font=BUTTON_FONT, command=self.zoomOut)
        self.zoomInButton.pack()
        self.zoomOutButton.pack()

    def zoomIn(self):
        self.canvasZoom += 1
        self.updateCanvasSize()

    def zoomOut(self): #TODO if canvas is already zoomed out, dont get smaller. Use widths to change sizes
        self.canvasZoom -= 1
        self.updateCanvasSize()


    def drawCanvasGrid(self):
        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0] + 1):
            if x != self.gridSize[0] / 2:
                line = self.canvas.create_line(x * self.canvasZoom, 0, x * self.canvasZoom, self.canvasHeight, width=1,
                                           fill=fillColor)
        for y in range(0, self.gridSize[1] + 1):
            if y != self.gridSize[1] / 2:
                line = self.canvas.create_line(0, y * self.canvasZoom, self.canvasWidth, y * self.canvasZoom, width=1,
                                           fill=fillColor)
        border = self.canvas.create_rectangle(0, 0, self.canvasHeight, self.canvasWidth, outline='Orange', width=2)

    def drawCanvasAxes(self):
        if self.gridSize[0] % 2 == 0:
            yAxis = self.canvas.create_line(self.canvasWidth / 2, 0, self.canvasWidth / 2, self.canvasHeight, width=1,
                                            fill="#00cc00")
        else:
            yAxis = self.canvas.create_rectangle((self.canvasWidth / 2) - (self.canvasZoom / 2), 0,
                                                 (self.canvasWidth / 2) + (self.canvasZoom / 2), self.canvasHeight,
                                                 fill="#e6ffe6", width=0)
        if self.gridSize[1] % 2 == 0:
            xAxis = self.canvas.create_line(0, self.canvasHeight / 2, self.canvasWidth, self.canvasHeight / 2, width=1,
                                            fill="red")
        else:
            xAxis = self.canvas.create_rectangle(0, (self.canvasHeight / 2) - (self.canvasZoom / 2), self.canvasWidth,
                                                 (self.canvasHeight / 2) + (self.canvasZoom / 2), fill="#ffe6e6",
                                                 width=0)

        if self.gridSize[0] % 2 != 0 and self.gridSize[1] % 2 != 0:
            print("Both?")
            origin = self.canvas.create_rectangle((self.canvasWidth / 2) - (self.canvasZoom / 2), (self.canvasHeight / 2) - (self.canvasZoom / 2), (self.canvasWidth / 2) + (self.canvasZoom / 2), (self.canvasHeight / 2) + (self.canvasZoom / 2), fill="#cce0ff", width=0)

    def drawRectangleHere(self,x,y,color="red"): #TODO create new coordinate system. Origin at center? how to translate to in-game coords?
        border = 2
        self.canvas.create_rectangle(x+border,y+border,(x+self.canvasZoom)-border,(y+self.canvasZoom)-border,fill="red", width=0)

root = Tk()

#size of the window


app = Window(root)
rootSize = str(600) + "x" + str(600)
root.geometry(rootSize)
root.mainloop()
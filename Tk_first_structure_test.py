from tkinter import *
import random


LABEL_FONT = ("Times","30","bold")





class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.canvasZoom = 20 # Pixels per square in the grid
        self.gridSize = [50,50] # number of squares in the grid

        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title
        self.master.title("MINECRAFT SPHERE CALCULATOR")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #Label

        labelText = "Minecraft Sphere Calculator"
        if random.randint(0,200) == 0:
            labelText = "MINCERAFT Sphere Calculator"

        topLabel = Label(self, text=labelText, font=LABEL_FONT)
        topLabel.pack()

        self.drawBlankCanvas()
        self.drawCanvasGrid()


    def drawBlankCanvas(self):
        self.canvasFrame = Frame(self,bd=10,relief=SUNKEN)
        self.canvasWidth = (self.canvasZoom * self.gridSize[0])    # - 8
        self.canvasHeight = (self.canvasZoom * self.gridSize[1])    # - 5
        self.canvas = Canvas(self.canvasFrame, width=self.canvasWidth, height=self.canvasHeight, bg='white')

        #self.canvas.create_rectangle(0,0,self.canvasWidth,self.canvasHeight,fill='red')

        self.canvas.grid(row=0, column=0)

        scroll_x = Scrollbar(self.canvasFrame, orient="horizontal", command=self.canvas.xview)
        scroll_x.grid(row=1, column=0, sticky=EW)

        scroll_y = Scrollbar(self.canvasFrame, orient="vertical", command=self.canvas.yview)
        scroll_y.grid(row=0, column=1, sticky=NS)

        self.canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) ##TODO fix scrolling
        self.canvas.grid()

        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.rowconfigure(0, weight=1)
        self.canvasFrame.pack(fill=X)

    def drawCanvasGrid(self):
        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0]+1):
            line = self.canvas.create_line(x*self.canvasZoom, 0, x*self.canvasZoom, self.canvasHeight,width=1,fill=fillColor)
        for y in range(0, self.gridSize[1]+1):
            line = self.canvas.create_line(0,y*self.canvasZoom, self.canvasWidth, y*self.canvasZoom, width=1,fill=fillColor)

root = Tk()

#size of the window


app = Window(root)
rootSize = str(900) + "x" + str(900)
root.geometry(rootSize)
root.mainloop()
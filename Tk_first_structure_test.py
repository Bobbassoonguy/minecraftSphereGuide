from tkinter import *
import random


LABEL_FONT = ("Times","30","bold")





class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.gridSize = [30,30] # number of squares in the grid

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
        topLabel.grid(row=0)

        self.canvasWidth = 0
        self.canvasHeight = 0
        self.canvasZoom = 20

        self.drawBlankCanvas()
        self.bind("<Configure>", self.resizeCanvas)

        self.drawCanvasGrid()



    def drawBlankCanvas(self):
        self.canvasFrame = Frame(self,bd=10,relief=SUNKEN)
        self.canvasFrame.grid(row=2)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        # self.canvasZoom = 20  # Pixels per square in the grid
        # Pixels per square in the grid = width of grid space / gridsize x
        # self.canvasZoom = self.grid_bbox(column=0,row=2)[2]/self.gridSize[0]
        self.canvas = Canvas(self.canvasFrame, width=self.canvasWidth, height=self.canvasHeight, bg='white')

        self.canvas.create_oval(10, 10, 20, 20, fill="red")
        self.canvas.create_oval(200, 200, 220, 220, fill="blue")
        self.canvas.create_oval(1400, 1400, 1410, 1410, fill="green")
        # self.canvas.create_rectangle(0,0,self.canvasWidth,self.canvasHeight,fill='red')

        self.canvas.grid(row=0, column=0)

        self.canvasScrolling()

        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.rowconfigure(0, weight=1)


    def resizeCanvas(self, event):
        print("resize")
        usableWidth = event.width - 50
        if abs(usableWidth - self.canvasWidth) > 20:
            self.canvasZoom = round(usableWidth / self.gridSize[0])
            self.canvasWidth = (self.canvasZoom * self.gridSize[0])
            self.canvasHeight = (self.canvasZoom * self.gridSize[1])

            # self.canvasFrame.destroy() ##TODO Figure out why when x is smaller than y, canvases layer. Figure out how to kill canvas properly
            self.drawBlankCanvas()
            # self.drawCanvasGrid()



    def canvasScrolling(self):
        scroll_x = Scrollbar(self.canvasFrame, orient="horizontal", command=self.canvas.xview)
        scroll_x.grid(row=1, column=0, sticky=EW)
        scroll_y = Scrollbar(self.canvasFrame, orient="vertical", command=self.canvas.yview)
        scroll_y.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        # self.canvas.configure(scrollregion=self.canvas.bbox("all"))  ##TODO fix scrolling
        self.canvas.configure(scrollregion=(0,0,self.canvasWidth,self.canvasHeight))  ##TODO fix scrolling
        self.canvas.grid()


    def drawCanvasGrid(self):
        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0]+1):
            line = self.canvas.create_line(x*self.canvasZoom, 0, x*self.canvasZoom, self.canvasHeight,width=1,fill=fillColor)
        for y in range(0, self.gridSize[1]+1):
            line = self.canvas.create_line(0,y*self.canvasZoom, self.canvasWidth, y*self.canvasZoom, width=1,fill=fillColor)
        border = self.canvas.create_rectangle(0,0,self.canvasHeight,self.canvasWidth,outline='Orange',width=2)

root = Tk()

#size of the window


app = Window(root)
rootSize = str(800) + "x" + str(800)
root.geometry(rootSize)
root.mainloop()
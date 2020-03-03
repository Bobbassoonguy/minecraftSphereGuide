from tkinter import *


class squareDispCanvas():
    def __init__(self, master=None):
        self.master = master

        self.gridSize = [200, 200]
        self.canvasHeight = 600
        self.canvasWidth = (self.canvasHeight / self.gridSize[1]) * self.gridSize[0]
        self.canvasSquareSize = int(self.canvasHeight / self.gridSize[1])

        self.frame = Frame(self.master, bd=10, relief=SUNKEN, bg="green")
        self.frame.grid(row=2, sticky=NSEW)

        master.rowconfigure(2, weight=1)  # TODO move this out of class
        master.columnconfigure(0, weight=1)  # TODO move this out of class

        self.canvas = Canvas(self.frame, width=self.canvasWidth, height=self.canvasHeight, bg='white')
        self.canvas.grid(row=0, column=0)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # self.canvasScrolling()
        # self.canvasZoomButtons()
        # self.drawCanvasAxes()
        # self.drawCanvasGrid()

        # self.canvas.bind("<MouseWheel>", self.mouseWheel)
        # self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        # self.canvas.bind("<B1-Motion>", self.scroll_move)
        self.canvas.bind("<Configure>", self.resizeCanvas)

    def mouseWheel(self, event):
        scroll = event.delta
        if abs(scroll) > 100:
            scroll = -1 * int(scroll / 120)

        # self.canvas.yview(SCROLL, scroll, UNITS)

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def resizeCanvas(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.canvasWidth
        hscale = float(event.height) / self.canvasHeight
        self.canvasWidth = event.width
        self.canvasHeight = event.height
        # resize the canvas
        self.canvas.config(width=self.canvasWidth, height=self.canvasHeight)
        # rescale all the objects tagged with the "all" tag
        self.canvas.scale("all", 0, 0, wscale, hscale)

        # canvAndSpaceDiff = abs(self.frame.grid_bbox(column=0, row=0)[3] - self.canvasHeight)
        # if 10 < canvAndSpaceDiff < 30:
        #     self.canvasHeight = self.frame.grid_bbox(column=0, row=0)[3]
        #     self.canvasWidth = (self.canvasHeight / self.gridSize[1]) * self.gridSize[0]
        #     self.canvas.configure(width=self.canvasWidth, height=self.canvasHeight)

        # self.canvas.configure(scrollregion=(0, 0, self.canvasWidth, self.canvasHeight))
        # self.canvas.configure(scrollregion=(self.canvas.bbox("all")[0], self.canvas.bbox("all")[1], self.canvas.bbox("all")[2], self.canvas.bbox("all")[3]))

    def canvasScrolling(self):  # TODO change scrolling to canvasZoom
        self.scroll_x = Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky=EW)
        self.scroll_y = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        self.canvas.configure(scrollregion=(0, 0, self.canvasWidth, self.canvasHeight))
        self.canvas.grid()

    def canvasZoomButtons(self):  # TODO "fill" frame button
        self.canvasZoomButtonFrame = Frame(self.frame)
        self.canvasZoomButtonFrame.grid(column=2, row=0, sticky=N)

        self.zoomInButton = Button(self.canvasZoomButtonFrame, text="+", width=3, command=self.zoomIn)
        self.zoomOutButton = Button(self.canvasZoomButtonFrame, text="-", width=3, command=self.zoomOut)
        self.fillButton = Button(self.canvasZoomButtonFrame, text="Fill", width=3)

        self.zoomInButton.pack()
        self.zoomOutButton.pack()
        self.fillButton.pack()

    def zoomIn(self):  # TODO implement scaling vs redraw canvas
        self.canvas.scale("all", 0, 0, 1.1, 1.1)

    # TODO can't zoom out past maximum
    def zoomOut(self):  # TODO implement scaling vs redraw canvas
        self.canvas.scale("all", 0, 0, .9, .9)

    def drawCanvasGrid(self):
        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0] + 1):
            if x != self.gridSize[0] / 2:
                line = self.canvas.create_line(x * self.canvasSquareSize, 0, x * self.canvasSquareSize,
                                               self.canvasHeight, width=1,
                                               fill=fillColor)
        for y in range(0, self.gridSize[1] + 1):
            if y != self.gridSize[1] / 2:
                line = self.canvas.create_line(0, y * self.canvasSquareSize, self.canvasWidth,
                                               y * self.canvasSquareSize, width=1,
                                               fill=fillColor)
        border = self.canvas.create_rectangle(0, 0, self.canvasHeight, self.canvasWidth, outline='Orange', width=2)

    def drawCanvasAxes(self):
        if self.gridSize[0] % 2 == 0:
            yAxis = self.canvas.create_line(self.canvasWidth / 2, 0, self.canvasWidth / 2, self.canvasHeight, width=1,
                                            fill="#00cc00")
        else:
            yAxis = self.canvas.create_rectangle((self.canvasWidth / 2) - (self.canvasSquareSize / 2), 0,
                                                 (self.canvasWidth / 2) + (self.canvasSquareSize / 2),
                                                 self.canvasHeight,
                                                 fill="#e6ffe6", width=0)
        if self.gridSize[1] % 2 == 0:
            xAxis = self.canvas.create_line(0, self.canvasHeight / 2, self.canvasWidth, self.canvasHeight / 2, width=1,
                                            fill="red")
        else:
            xAxis = self.canvas.create_rectangle(0, (self.canvasHeight / 2) - (self.canvasSquareSize / 2),
                                                 self.canvasWidth,
                                                 (self.canvasHeight / 2) + (self.canvasSquareSize / 2), fill="#ffe6e6",
                                                 width=0)

        if self.gridSize[0] % 2 != 0 and self.gridSize[1] % 2 != 0:
            print("Both?")
            origin = self.canvas.create_rectangle((self.canvasWidth / 2) - (self.canvasSquareSize / 2),
                                                  (self.canvasHeight / 2) - (self.canvasSquareSize / 2),
                                                  (self.canvasWidth / 2) + (self.canvasSquareSize / 2),
                                                  (self.canvasHeight / 2) + (self.canvasSquareSize / 2), fill="#cce0ff",
                                                  width=0)




# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


root = Tk()
canv = squareDispCanvas(root)

# lifts window to top, but not permanently
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()

from tkinter import *


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)

        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

        self.scrollregion = (0, 0, self.width, self.height)

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        if (round(event.width) != round(self.width) or round(event.height) != round(self.height)) and not self.supressResize:
            if event.width > event.height:
                # print("Window wide")
                scale = float(event.width) / self.width
                self.width = event.width
                self.height = self.width
            else:
                # print("Window tall")
                scale = float(event.height) / self.height
                self.height = event.height
                self.width = self.height
            # resize the canvas, update scrollregion
            self.config(width=self.width, height=self.height, scrollregion=(0, 0, self.width, self.height))
            # rescale all the objects tagged with the "all" tag
            self.scale("all", 0, 0, scale, scale)

            print("resized:", self.width, ",", self.height, self.scrollregion)
        self.supressResize = False

    def zoom(self, scale): # TODO figure out why before window is ever resized, zoom changes window size
        self.supressResize = True

        # determine the ratio of old width/height to new width/height
        self.width = round(self.width * scale)
        self.height = self.width

        # resize the canvas, update scrollregion
        self.config(width=self.width, height=self.height, scrollregion=(0, 0, self.width, self.height))
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, scale, scale)
        print("Zoomed:", self.width, ",", self.height, self.scrollregion)

    def scroll_start(self, event):
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)


class SquareDispCanvas:
    def __init__(self, master=None):
        self.master = master

        self.gridSize = [99, 99]

        # Create display frame
        self.frame = Frame(self.master,bg="green")
        self.frame.grid(row=2, sticky=NSEW)
        master.rowconfigure(2, weight=1)  # TODO move this out of class
        master.columnconfigure(0, weight=1)  # TODO move this out of class

        # Create resizing canvas
        self.canvas = ResizingCanvas(self.frame, width=700, height=700, bg="red", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.canvasScrolling()
        self.canvasZoomButtons()

        self.drawCanvasGrid()
        self.drawCanvasAxes()

    def drawCanvasGrid(self):
        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth/self.gridSize[0], canvasHeight/self.gridSize[1]]

        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0] + 1):
            if x != self.gridSize[0] / 2:
                self.canvas.create_line(x * squareSize[0], 0, x * squareSize[0], canvasHeight, width=1, fill=fillColor)
        for y in range(0, self.gridSize[1] + 1):
            if y != self.gridSize[1] / 2:
                self.canvas.create_line(0, y * squareSize[1], canvasWidth, y * squareSize[1], width=1, fill=fillColor)
        self.canvas.create_rectangle(0, 0, canvasHeight, canvasWidth, outline='Orange', width=2)

    def drawCanvasAxes(self):
        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth/self.gridSize[0], canvasHeight/self.gridSize[1]]
        if self.gridSize[0] % 2 == 0:
            yAxis = self.canvas.create_line(canvasWidth / 2, 0, canvasWidth / 2, canvasHeight, width=1,
                                            fill="#00cc00")
        else:
            yAxis = self.canvas.create_rectangle((canvasWidth / 2) - (squareSize[0] / 2), 0,
                                                 (canvasWidth / 2) + (squareSize[0] / 2),
                                                 canvasHeight,
                                                 fill="#e6ffe6", width=0)
        if self.gridSize[1] % 2 == 0:
            xAxis = self.canvas.create_line(0, canvasHeight / 2, canvasWidth, canvasHeight / 2, width=1,
                                            fill="red")
        else:
            xAxis = self.canvas.create_rectangle(0, (canvasHeight / 2) - (squareSize[1] / 2),
                                                 canvasWidth,
                                                 (canvasHeight / 2) + (squareSize[1] / 2), fill="#ffe6e6",
                                                 width=0)

        if self.gridSize[0] % 2 != 0 and self.gridSize[1] % 2 != 0:
            origin = self.canvas.create_rectangle((canvasWidth / 2) - (squareSize[0] / 2),
                                                  (canvasHeight / 2) - (squareSize[1] / 2),
                                                  (canvasWidth / 2) + (squareSize[0] / 2),
                                                  (canvasHeight / 2) + (squareSize[1] / 2), fill="#cce0ff",
                                                  width=0)

    def canvasScrolling(self):  # TODO change scrolling to canvasZoom
        self.scroll_x = Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky=EW)
        self.scroll_y = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
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

    def zoomIn(self):
        self.canvas.zoom(1.1)

    # TODO can't zoom out past maximum
    def zoomOut(self):
        self.canvas.zoom(.9)

    def fit(self):







root = Tk()

disp = SquareDispCanvas(root)

# lifts window to top, but not permanently
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()
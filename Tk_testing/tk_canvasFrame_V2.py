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





root = Tk()

disp = SquareDispCanvas(root)

# lifts window to top, but not permanently
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()
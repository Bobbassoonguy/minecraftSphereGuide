from tkinter import *
import colorsys
from Carson_Logic import sphereFormatted


def RGB(red, green, blue): return '#%02x%02x%02x' % (red, green, blue)


def drawRainbow(rad):
    rainbowList = []
    for hue in range(0, 1000, int(1000 / rad)):
        (r, g, b) = colorsys.hsv_to_rgb(hue / 1000, 1.0, 1.0)
        R, G, B = int(255 * r), int(255 * g), int(255 * b)
        rainbowList.append(RGB(R, G, B))
    return rainbowList


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

        self.bind("<Configure>", self.on_resize)
        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)
        self.bind("<MouseWheel>", self.mouseWheel)

        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

        self.scrollregion = (0, 0, self.width, self.height)

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        if (round(event.width) != round(self.width) or round(event.height) != round(
                self.height)) and not self.supressResize:
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

    def zoom(self, scale):  # TODO figure out why before window is ever resized, zoom changes window size
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

    def mouseWheel(self, event):
        scroll = event.delta
        if abs(scroll) > 100:
            scroll = -1 * int(scroll / 120)

        if (scroll > 0):
            self.zoom(1.05)
        elif (scroll < 0):
            self.zoom(.95)

    def clearAll(self):
        self.addtag_all("all")
        self.delete("all")


class SquareDispCanvas:
    def __init__(self, master=None, radius=16, pFrame=None):
        self.master = master
        self.pFrame = pFrame

        self.gridSize = [radius, radius]
        self.originLoc = "SW"

        # Create display frame
        self.frame = Frame(self.master, relief=SUNKEN, bd=4)
        self.frame.grid(row=2, sticky=NSEW)  # TODO move this out of class
        master.rowconfigure(2, weight=1)  # TODO move this out of class
        master.columnconfigure(0, weight=1)  # TODO move this out of class

        # Create resizing canvas
        self.canvas = ResizingCanvas(self.frame, width=radius * 10, height=radius * 10, bg="white",
                                     highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.canvasScrolling()
        self.canvasZoomButtons()

        self.canvas.tag_bind("rectangle", '<Enter>', self.onRectEnter)


    def drawCanvasGrid(self):
        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth / self.gridSize[0], canvasHeight / self.gridSize[1]]

        fillColor = "#cccccc"
        for x in range(0, self.gridSize[0] + 1):
            self.canvas.create_line(x * squareSize[0], 0, x * squareSize[0], canvasHeight, width=1, fill=fillColor)
        for y in range(0, self.gridSize[1] + 1):
            self.canvas.create_line(0, y * squareSize[1], canvasWidth, y * squareSize[1], width=1, fill=fillColor)
        # self.canvas.create_rectangle(0, 0, canvasHeight, canvasWidth, outline='Orange', width=1)

    def drawCanvasAxes(self):
        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth / self.gridSize[0], canvasHeight / self.gridSize[1]]
        axisWidth = 6

        if self.originLoc == "SW":
            yAxis = self.canvas.create_line(0, 0, 0, canvasHeight, width=axisWidth,
                                            fill="#00cc00")
            xAxis = self.canvas.create_line(0, canvasHeight, canvasWidth, canvasHeight, width=axisWidth, fill="red")
        elif self.originLoc == "SE":
            yAxis = self.canvas.create_line(canvasWidth, 0, canvasWidth, canvasHeight, width=axisWidth,
                                            fill="#00cc00")
        elif self.originLoc == "NW":
            xAxis = self.canvas.create_line(0, 0, canvasWidth, 0, width=axisWidth, fill="red")
        elif self.originLoc == "NE":
            print("No Axes")

        # if type(self.gridSize[0]) is int:
        #     print("X is int")
        #     yAxis = self.canvas.create_line(0, 0, 0, canvasHeight, width=4,
        #                                     fill="#00cc00")
        # else:
        #     yAxis = self.canvas.create_rectangle(0, 0, squareSize[0], canvasHeight, fill="#e6ffe6", width=0)
        # if type(self.gridSize[1]) is int:
        #     xAxis = self.canvas.create_line(0, canvasHeight, canvasWidth, canvasHeight, width=4, fill="red")
        # else:
        #     xAxis = self.canvas.create_rectangle(0, canvasHeight - squareSize[1], canvasWidth, canvasHeight,
        #                                          fill="#ffe6e6", width=0)

        # if self.gridSize[0] % 2 != 0 and self.gridSize[1] % 2 != 0:
        #     origin = self.canvas.create_rectangle((canvasWidth / 2) - (squareSize[0] / 2),
        #                                           (canvasHeight / 2) - (squareSize[1] / 2),
        #                                           (canvasWidth / 2) + (squareSize[0] / 2),
        #                                           (canvasHeight / 2) + (squareSize[1] / 2), fill="#cce0ff",
        #                                           width=0)

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
        self.fillButton = Button(self.canvasZoomButtonFrame, text="Fill", width=3, command=self.fit)

        self.zoomInButton.pack()
        self.zoomOutButton.pack()
        self.fillButton.pack()

    def zoomIn(self):
        self.canvas.zoom(1.1)

    # TODO can't zoom out past maximum
    def zoomOut(self):
        self.canvas.zoom(.9)

    def fit(self):
        canvYRoom = self.frame.grid_bbox(0, 0)[3]
        canvXRoom = self.frame.grid_bbox(0, 0)[2]
        # determine the ratio of old width/height to new width/height
        if canvXRoom > canvYRoom:
            # print("Window wide")
            scale = float(canvYRoom) / self.canvas.height
            self.canvas.height = canvYRoom
            self.canvas.width = self.canvas.height
        else:
            # print("Window tall")
            scale = float(canvXRoom) / self.canvas.width
            self.canvas.width = canvXRoom
            self.canvas.height = self.canvas.width
        # resize the canvas, update scrollregion
        self.canvas.config(width=self.canvas.width, height=self.canvas.height,
                           scrollregion=(0, 0, self.canvas.width, self.canvas.height))
        # rescale all the objects tagged with the "all" tag
        self.canvas.scale("all", 0, 0, scale, scale)

        print("fit:", self.canvas.width, ",", self.canvas.height, self.canvas.scrollregion)

    def gridToCanvCoords(self, coords):
        x = coords[0]
        y = coords[1]

        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth / self.gridSize[0], canvasHeight / self.gridSize[1]]

        if self.originLoc == "SW":
            x = x * squareSize[0]
            y = self.canvas.height - ((y + 1) * squareSize[1])
        elif self.originLoc == "SE":
            x = canvasWidth + (x * squareSize[0])
            y = self.canvas.height - ((y + 1) * squareSize[1])
        elif self.originLoc == "NW":
            x = x * squareSize[0]
            y = ((-1 * (y + 1)) * squareSize[1])
        elif self.originLoc == "NE":
            x = canvasWidth + (x * squareSize[0])
            y = ((-1 * (y + 1)) * squareSize[1])

        return [x, y]

    def drawRect(self, coords, small=True, color="red"):
        canvasHeight = self.canvas.height
        canvasWidth = self.canvas.width
        squareSize = [canvasWidth / self.gridSize[0], canvasHeight / self.gridSize[1]]

        CanvCoords = self.gridToCanvCoords(coords)

        border = .5
        if small:
            border = 3

        self.canvas.create_rectangle(CanvCoords[0] + border, CanvCoords[1] + border, (CanvCoords[0] + squareSize[0]) - border,
                                     (CanvCoords[1] + squareSize[1]) - border, fill=color, width=0, tags=("rectangle",("x"+str(coords[0])), ("y"+str(coords[1]))),
                                     activestipple="gray75")

    def drawTheseRectangles(self, coords, color="red"):

        for pair in coords:
            if self.originLoc == "SW":
                if pair[0] >= 0 and pair[1] >= 0:
                    self.drawRect(pair, small=False, color=color)
            elif self.originLoc == "SE":
                if pair[0] <= 0 and pair[1] >= 0:
                    self.drawRect(pair, small=False, color=color)
            elif self.originLoc == "NW":
                if pair[0] >= 0 and pair[1] <= 0:
                    self.drawRect(pair, small=False, color=color)
            elif self.originLoc == "NE":
                if pair[0] <= 0 and pair[1] <= 0:
                    self.drawRect(pair, small=False, color=color)

    def updateRadius(self, newRad):
        if type(int(newRad)) is int:
            newRad = int(newRad)
            self.gridSize = [newRad, newRad]
            self.canvas.clearAll()
            self.canvas.config(width=newRad * 10, height=newRad * 10)

            self.drawCanvasGrid()
            self.drawCanvasAxes()

    def removeRectangles(self):
        self.canvas.delete("rectangle")

    def onRectEnter(self, event):
        print('Got object Enter', event.x, event.y)
        overlapping = event.widget.find_overlapping(event.x+1, event.y+1,event.x-1, event.y-1)
        foundRectangle = False
        for i in overlapping:
            tags = event.widget.gettags(i)
            if "rectangle" in tags:
                print(tags)
                foundRectangle = True
                break
        if not foundRectangle:
            print("No rectangle found")

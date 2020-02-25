from tkinter import *
import random


LABEL_FONT = ("Times","30","bold")





class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
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


    def drawBlankCanvas(self):
        self.canvasFrame = Frame(self,bd=10,relief=SUNKEN)
        canvas = Canvas(self.canvasFrame, width=1500, height=1500, bg='white')
        canvas.create_oval(10, 10, 20, 20, fill="red")
        canvas.create_oval(200, 200, 220, 220, fill="blue")
        canvas.create_oval(1400, 1400, 1410, 1410, fill="green")
        canvas.grid(row=0, column=0)

        scroll_x = Scrollbar(self.canvasFrame, orient="horizontal", command=canvas.xview)
        scroll_x.grid(row=1, column=0, sticky=EW)

        scroll_y = Scrollbar(self.canvasFrame, orient="vertical", command=canvas.yview)
        scroll_y.grid(row=0, column=1, sticky=NS)

        canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.grid()

        self.canvasFrame.columnconfigure(0, weight=1)
        self.canvasFrame.rowconfigure(0, weight=1)
        self.canvasFrame.pack(fill=X)



root = Tk()

#size of the window
root.geometry("800x800")

app = Window(root)
root.mainloop()
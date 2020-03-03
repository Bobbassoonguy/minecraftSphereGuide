from tkinter import *
from tkinter import ttk
import tk_canvasFrame

#root application, can only have one of these.
root = Tk()
#put a label in the root to identify the window.
label1 = Label(root, text="""this is root
closing this window will shut down app""")
label1.grid(row=0)

canv = tk_canvasFrame.squareDispCanvas(root)

def howBigIsFrame():
    print(canv.frame.grid_bbox(column=0,row=0))

button1 = Button(root, text="this is a button",command=howBigIsFrame)
button1.grid(row=1)


#you can make as many Toplevels as you like
extra_window = Toplevel(root)
label2 = Label(extra_window, text="""this is extra_window
closing this will not affect root""")
label2.pack()
root.mainloop()
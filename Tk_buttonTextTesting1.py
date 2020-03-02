from tkinter import *
from tkinter import ttk

#root application, can only have one of these.
root = Tk()
#put a label in the root to identify the window.
label1 = Label(root, text="""this is root
closing this window will shut down app""")
label1.pack()

button1 = Button(root, text="this is a button")
button1.pack()


#you can make as many Toplevels as you like
extra_window = Toplevel(root)
label2 = Label(extra_window, text="""this is extra_window
closing this will not affect root""")
label2.pack()
root.mainloop()
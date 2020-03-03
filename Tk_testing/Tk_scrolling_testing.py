try:
 import tkinter as tk #python3
except ImportError:
 import Tkinter as tk #python2
#root application, can only have one of these.
root = tk.Tk()
#put a label in the root to identify the window.
label1 = tk.Label(root, text="""this is root
closing this window will shut down app""")
label1.pack()
#you can make as many Toplevels as you like
extra_window = tk.Toplevel(root)
label2 = tk.Label(extra_window, text="""this is extra_window closing this will not affect root""")

canvas = tk.Canvas(extra_window, width=150, height=150)
canvas.create_oval(10, 10, 20, 20, fill="red")
canvas.create_oval(200, 200, 220, 220, fill="blue")
canvas.grid(row=0, column=0)
scroll_x = tk.Scrollbar(extra_window, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")
scroll_y = tk.Scrollbar(extra_window, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
canvas.configure(scrollregion=canvas.bbox("all"))

label2.grid()
canvas.grid()

root.mainloop()

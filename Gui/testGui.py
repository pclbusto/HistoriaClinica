from tkinter import *
from tkinter import Tk, ttk, Frame

root = Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
frame = Frame(root,bg='green',height=300, width=100)
frame.grid(sticky=(N,W,E,S))
root.mainloop()

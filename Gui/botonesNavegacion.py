from iconos import Iconos
import PIL.Image, PIL.ImageTk
from tkinter import Frame,Button,Label

class PanelNavegacion(Frame):


    def __init__(self, parent, cnf={}, **kw):
        Frame.__init__(self, parent, cnf, **kw)

        # GENERAMOS BOTONES DE NAVEGACION
        self.pilImageFirst = Iconos.Iconos.pilImageFirst
        self.imageFirst = PIL.ImageTk.PhotoImage(self.pilImageFirst)
        self.botonFirst = Button(self, image=self.imageFirst)
        self.botonFirst.grid(row=0, column=0)
        self.pilImagePrev = Iconos.Iconos.pilImagePrev
        self.imagePrev = PIL.ImageTk.PhotoImage(self.pilImagePrev)
        self.botonPrev = Button(self, image=self.imagePrev)
        self.botonPrev.grid(row=0, column=1)
        self.statusLabel = Label(self,width=20,text='01/01/1900').grid(row=0,column=2)
        self.pilImageNext = Iconos.Iconos.pilImageNext
        self.imageNext = PIL.ImageTk.PhotoImage(self.pilImageNext)
        self.botonNext = Button(self, image=self.imageNext)
        self.botonNext.grid(row=0, column=3)
        self.pilImageLast = Iconos.Iconos.pilImageLast
        self.imageLast = PIL.ImageTk.PhotoImage(self.pilImageLast)
        self.botonLast = Button(self, image=self.imageLast)
        self.botonLast.grid(row=0, column=4)

    def setStatusLabel(self,texto):
        print(self.statusLabel)
        self.statusLabel.config(text=texto)

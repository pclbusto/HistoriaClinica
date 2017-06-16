from tkinter import *
from tkinter import Tk, ttk, Frame
from iconos import Iconos
import PIL.Image, PIL.ImageTk

class FrameGenerico(Frame):
    def __init__(self, parent, cnf={}, **kw):
        Frame.__init__(self, parent, cnf, **kw)
        # CREAMOS DOS ZONAS. LA DEL PANEL Y LA BOTONERA DE ACCIONES Y NAVEGACION
        self.panelPrincipal=Frame(self)
        self.panelPrincipal.grid(row=0,column=0,sticky=E+W+S+N)

        self.panelNavelgacion = Frame(self)
        self.panelNavelgacion.grid(row=1, column=0, sticky=E + W + S + N)

        #GENERAMOS BOTONES DE NAVEGACION
        self.frameBotonesNavegacion = Frame(self.panelNavelgacion)
        self.frameBotonesNavegacion.grid(row=0, column=0, sticky=W)
        self.pilImageFirst = Iconos.Iconos.pilImageFirst
        self.imageFirst = PIL.ImageTk.PhotoImage(self.pilImageFirst)
        self.botonFirst = Button(self.frameBotonesNavegacion, image=self.imageFirst)
        self.botonFirst.grid(row=0, column=0)
        self.pilImagePrev = Iconos.Iconos.pilImagePrev
        self.imagePrev = PIL.ImageTk.PhotoImage(self.pilImagePrev)
        self.botonPrev = Button(self.frameBotonesNavegacion, image=self.imagePrev)
        self.botonPrev.grid(row=0, column=1)
        self.pilImageNext = Iconos.Iconos.pilImageNext
        self.imageNext = PIL.ImageTk.PhotoImage(self.pilImageNext)
        self.botonNext = Button(self.frameBotonesNavegacion, image=self.imageNext)
        self.botonNext.grid(row=0, column=2)
        self.pilImageLast = Iconos.Iconos.pilImageLast
        self.imageLast = PIL.ImageTk.PhotoImage(self.pilImageLast)
        self.botonLast = Button(self.frameBotonesNavegacion, image=self.imageLast)
        self.botonLast.grid(row=0, column=3)

        # GENERAMOS BOTONES DE ACCIONES GUARDAR, BORRAR ELIMINAR
        self.frameBotonesAcciones = Frame(self.panelNavelgacion)

        self.frameBotonesAcciones.grid(row=0, column=1, sticky=E)
        self.botonGuardar = Button(self.frameBotonesAcciones, text="Guardar")
        self.botonGuardar.grid(row=0, column=0, sticky=E)
        self.botonGuardar = Button(self.frameBotonesAcciones, text="Borrar")
        self.botonGuardar.grid(row=0, column=1, sticky=E)
        self.botonGuardar = Button(self.frameBotonesAcciones, text="Eliminar")
        self.botonGuardar.grid(row=0, column=2, sticky=E)
        self.botonGuardar = Button(self.frameBotonesAcciones, text="Cargar desde Web")
        self.botonGuardar.grid(row=0, column=3, sticky=E)
    def getPanelPrincipal(self):
        return self.panelPrincipal

class Paciente(FrameGenerico):
    def __init__(self, parent, cnf={}, **kw):
        FrameGenerico.__init__(self, parent, cnf, **kw)
        Label(self.getPanelPrincipal(),text="Nombre").grid(row=0,column=0)


if __name__ == '__main__':
    root = Tk()
    publisher = Paciente(root, width=507, height=358)
    publisher.pack()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    root.mainloop()
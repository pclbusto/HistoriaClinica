from tkinter import *
from tkinter import Tk, ttk, Frame
import PIL.Image, PIL.ImageTk
from iconos import Iconos
from Gui import FrameGenerico as fg
from datetime import datetime

class Paciente(fg.FrameGenerico):
    def __init__(self, parent, cnf={}, **kw):
        fg.FrameGenerico.__init__(self, parent, cnf, **kw)
        panelPrincipal = self.getPanelPrincipal()
        Label(panelPrincipal,text="Nombre").grid(row=0,column=0)
        self.entradaNombre = Entry(panelPrincipal)
        self.entradaNombre.grid(row=0,column=1,columnspan=2,sticky=E+W)
        Label(panelPrincipal, text="Apellido").grid(row=0, column=3)
        self.entradaApellido = Entry(panelPrincipal)
        self.entradaApellido.grid(row=0, column=4)
        Label(panelPrincipal, text="Sexo").grid(row=0, column=5)
        self.comboBoxSexo = ttk.Combobox(panelPrincipal,values=("Femenino","Masculino"))
        self.comboBoxSexo.grid(row=0, column=6)
        Label(panelPrincipal, text="Nivel Educativo").grid(row=1, column=0)
        self.entradaNivelEducativo = Entry(panelPrincipal)
        self.entradaNivelEducativo.grid(row=1, column=1,columnspan=2,sticky=E+W)
        Label(panelPrincipal, text="Fecha Nacimiento").grid(row=1, column=3)
        self.stringVarFechaNacimiento =StringVar()
        self.stringVarFechaNacimiento.set("01/01/1900")

        self.entradaFechaNacimiento = Entry(panelPrincipal,textvariable=self.stringVarFechaNacimiento)
        self.entradaFechaNacimiento.bind("<FocusOut>", self.entradaFechaNacimientoPosEvent)
        self.entradaFechaNacimiento.grid(row=1, column=4)

        Label(panelPrincipal, text="Documento").grid(row=2, column=0)
        self.entradaDocumento = Entry(panelPrincipal)
        self.entradaDocumento.grid(row=2, column=1)

        self.checkBoxObraSocial=ttk.Checkbutton(panelPrincipal,text="Tiene obra social")
        self.checkBoxObraSocial.grid(row=2,column=2)

        Label(panelPrincipal, text="Obra social").grid(row=2, column=3)
        self.entradaObraSocial = Entry(panelPrincipal)
        self.entradaObraSocial.grid(row=2, column=4)

        Label(panelPrincipal, text="Nro afiliado").grid(row=2, column=5)
        self.entradaNroAfiliado = Entry(panelPrincipal)
        self.entradaNroAfiliado.grid(row=2, column=6)

        Label(panelPrincipal, text="Dirección").grid(row=3, column=0)
        self.entradaDireccion = Entry(panelPrincipal)
        self.entradaDireccion.grid(row=3, column=1)

    def entradaFechaNacimientoPosEvent(self,event):
        cadena = self.stringVarFechaNacimiento.get()
        if cadena.rfind("/"):
            cadena = cadena.replace("/", "")
        if cadena.rfind("-"):
            cadena = cadena.replace("-", "")
        try:
            struct_time = datetime.strptime(cadena, "%d%m%Y")
        except ValueError as e:
            self.stringVarFechaNacimiento.set("01/01/1900")

if __name__ == '__main__':
    root = Tk()
    publisher = Paciente(root, width=507, height=358)
    publisher.pack()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    root.mainloop()


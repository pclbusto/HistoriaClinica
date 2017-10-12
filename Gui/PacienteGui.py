from tkinter import *
from tkinter import Tk, ttk
from Gui import FrameGenerico as fg
from datetime import datetime
from Entidades.Paciente import Paciente
from Entidades import Init
from sqlalchemy import func
from iconos import Iconos
import PIL.Image, PIL.ImageTk
from Gui.botonesNavegacion import PanelNavegacion

class PacienteGui(fg.FrameGenerico):
    def __init__(self, parent, cnf={}, **kw):
        fg.FrameGenerico.__init__(self, parent, cnf, **kw)
        self.session = Init.getSession()
        self.listaSexo=['Femenino','Masculino']
        self.registroNuevo=False
        self.offset=0
        self.cantidadRegistros = self.session.query(Paciente).count()
        self.varChecktieneObraSocial = IntVar()

        panelPrincipal = self.getPanelPrincipal()
        Label(panelPrincipal,text="Nombre").grid(row=0,column=0,sticky=W)
        self.entradaNombre = Entry(panelPrincipal)
        self.entradaNombre.grid(row=0,column=1,columnspan=2,sticky=E+W)
        Label(panelPrincipal, text="Apellido").grid(row=0, column=3,sticky=W)
        self.entradaApellido = Entry(panelPrincipal)
        self.entradaApellido.grid(row=0, column=4)
        Label(panelPrincipal, text="Sexo").grid(row=0, column=5)
        self.comboBoxSexo = ttk.Combobox(panelPrincipal, values=self.listaSexo)
        self.comboBoxSexo.grid(row=0, column=6)
        Label(panelPrincipal, text="Nivel Educativo").grid(row=1, column=0,sticky=W)
        self.entradaNivelEducativo = Entry(panelPrincipal)
        self.entradaNivelEducativo.grid(row=1, column=1,columnspan=2,sticky=E+W)
        Label(panelPrincipal, text="Fecha Nacimiento").grid(row=1, column=3,sticky=W)
        self.stringVarFechaNacimiento =StringVar()
        self.stringVarFechaNacimiento.set("01/01/1900")

        self.entradaFechaNacimiento = Entry(panelPrincipal,textvariable=self.stringVarFechaNacimiento)
        self.entradaFechaNacimiento.bind("<FocusOut>", self.entradaFechaNacimientoPosEvent)
        self.entradaFechaNacimiento.grid(row=1, column=4)

        Label(panelPrincipal, text="Documento").grid(row=2, column=0,sticky=W)
        self.entradaDocumento = Entry(panelPrincipal)
        self.entradaDocumento.grid(row=2, column=1,sticky=E+W)

        self.checkBoxObraSocial=Checkbutton(panelPrincipal,text="Tiene obra social",
                                            variable=self.varChecktieneObraSocial)
        self.checkBoxObraSocial.grid(row=2,column=2)

        Label(panelPrincipal, text="Obra social").grid(row=2, column=3,sticky=W)
        self.entradaObraSocial = Entry(panelPrincipal)
        self.entradaObraSocial.grid(row=2, column=4)

        Label(panelPrincipal, text="Nro afiliado").grid(row=2, column=5,sticky=W)
        self.entradaNroAfiliado = Entry(panelPrincipal)
        self.entradaNroAfiliado.grid(row=2, column=6)

        Label(panelPrincipal, text="Dirección").grid(row=3, column=0,sticky=W)
        self.entradaDireccion = Entry(panelPrincipal)
        self.entradaDireccion.grid(row=3, column=1, columnspan=2, sticky=(E, W))

        Label(panelPrincipal, text="motivo de consulta").grid(row=4, column=0,sticky=W)
        self.textMotivoConsulta = Text(panelPrincipal,height=5)
        self.textMotivoConsulta.grid(row=5, column=0, columnspan=7, sticky=(E, W))

        Label(panelPrincipal, text="Antecedentes").grid(row=6, column=0,sticky=W)
        self.textAntecedentes = Text(panelPrincipal,height=5)
        self.textAntecedentes.grid(row=7, column=0, columnspan=7, sticky=(N, E, S, W))

        Label(panelPrincipal, text="Problema Actual").grid(row=8, column=0,sticky=W)
        self.textProblemaActual = Text(panelPrincipal,height=5)
        self.textProblemaActual.grid(row=9, column=0,columnspan=7,sticky=(N,E,S,W))

        self.navegacionProblemaActual = PanelNavegacion(panelPrincipal)
        self.navegacionProblemaActual.grid(row=8, column=1, sticky=W)

        Label(panelPrincipal, text="Evaluación").grid(row=10, column=0,sticky=W)
        self.textEvaluacion = Text(panelPrincipal,height=5)
        self.textEvaluacion.grid(row=11, column=0,columnspan=7,sticky=(N,E,S,W))
        self.navegacionEvaluacion = PanelNavegacion(panelPrincipal)
        self.navegacionEvaluacion.grid(row=10, column=1, sticky=W)
        self.navegacionEvaluacion.setStatusLabel("Testing")


        Label(panelPrincipal, text="Evolución").grid(row=12, column=0,sticky=W)
        self.textEvolucion = Text(panelPrincipal,height=5)
        self.textEvolucion.grid(row=13, column=0,columnspan=7,sticky=(N,E,S,W))
        self.navegacionEvlucion = PanelNavegacion(panelPrincipal)
        self.navegacionEvlucion.grid(row=12, column=1, sticky=W)




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

    def guardar(self):
        super().guardar()
        print("guardando...")

        self.paciente.pacienteNombre = self.entradaNombre.get()
        self.paciente.pacienteApellido = self.entradaApellido.get()
        self.paciente.pacienteSexo = self.listaSexo.index(self.comboBoxSexo.get())
        self.paciente.pacienteNivelEducativo = self.entradaNivelEducativo.get()
        self.paciente.pacienteFechaNacimiento = 3214
        self.paciente.pacienteDocumento = self.entradaDocumento.get()
        self.paciente.pacienteTieneObraSocial = self.varChecktieneObraSocial.get()
        self.paciente.obraSocialNombre = self.entradaObraSocial.get()
        self.paciente.pacienteNroAfiliado = self.entradaNroAfiliado.get()
        self.paciente.pacienteDireccion = self.entradaDireccion.get()
        self.paciente.motivoConsulta = self.textMotivoConsulta.get(1.0,END)
        self.paciente.antecedentes = self.textAntecedentes.get(1.0,END)

        self.session.add(self.paciente)
        self.session.commit()
        self.cantidadRegistros = self.session.query(Paciente).count()

    def getNext(self):
        super().getNext()
        self.borrar()
        if self.offset <= self.cantidadRegistros:
            self.offset += 1
        print(self.offset)
        paciente = self.session.query(Paciente).order_by(func.lower(Paciente.pacienteApellido).asc()).offset(self.offset).first()
        if paciente is not None:
            self.paciente = paciente
            self.copyToWindow()

    def getLast(self):
        super().getLast()
        self.borrar()
        self.offset = self.cantidadRegistros-1
        paciente = self.session.query(Paciente).order_by(func.lower(Paciente.pacienteApellido).asc()).offset(self.offset).first()
        if paciente is not None:
            self.paciente = paciente
            self.copyToWindow()

    def getFirst(self):
        super().getFirst()
        self.borrar()
        self.offset = 0
        paciente = self.session.query(Paciente).order_by(func.lower(Paciente.pacienteApellido).asc()).offset(self.offset).first()
        if paciente is not None:
            self.paciente = paciente
            self.copyToWindow()

    def getPrev(self):
        super().getPrev()
        self.borrar()
        if self.offset > 0:
            self.offset -= 1
        print("Offset:{}".format(self.offset))
        paciente = self.session.query(Paciente).order_by(func.lower(Paciente.pacienteApellido).asc()).offset(self.offset).first()
        if paciente is not None:
            self.paciente = paciente
            self.copyToWindow()
        else:
            self.getFirst()

    def copyToWindow(self):
        self.entradaNombre.insert(0, self.paciente.pacienteNombre)
        self.entradaApellido.insert(0, self.paciente.pacienteApellido)
        self.comboBoxSexo.set(self.listaSexo[self.paciente.pacienteSexo])
        self.entradaNivelEducativo.insert(0, self.paciente.pacienteNivelEducativo)
        self.entradaFechaNacimiento.insert(0, self.paciente.pacienteFechaNacimiento)
        self.entradaDocumento.insert(0, self.paciente.pacienteDocumento)
        if self.paciente.pacienteTieneObraSocial:
            self.checkBoxObraSocial.select()
        else:
            self.checkBoxObraSocial.deselect()
        self.entradaObraSocial.insert(0, self.paciente.obraSocialNombre)
        self.entradaNroAfiliado.insert(0, self.paciente.pacienteNroAfiliado)
        self.entradaDireccion.insert(0, self.paciente.pacienteDireccion)
        self.textMotivoConsulta.insert(END, self.paciente.motivoConsulta)
        self.textAntecedentes.insert(END, self.paciente.antecedentes)
        self.registroNuevo = False

    def borrar(self):
        super().borrar()
        print("Limpiando formulario")
        self.paciente = Paciente()
        self.registroNuevo = True
        self.entradaNombre.delete(0, END)
        self.entradaApellido.delete(0, END)
        self.comboBoxSexo.set('')
        self.entradaNivelEducativo.delete(0,END)
        self.entradaFechaNacimiento.delete(0, END)
        self.entradaDocumento.delete(0, END)
        self.checkBoxObraSocial.deselect()
        self.entradaObraSocial.delete(0, END)
        self.entradaNroAfiliado.delete(0, END)
        self.entradaDireccion.delete(0, END)
        self.textMotivoConsulta.delete("0.0",END)
        self.textAntecedentes.delete("0.0",END)

if __name__ == '__main__':
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    paciente = PacienteGui(root, width=507, height=358)
    paciente.grid(sticky=(E, S, W, N))
    root.mainloop()


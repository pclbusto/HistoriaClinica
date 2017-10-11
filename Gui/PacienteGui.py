from tkinter import *
from tkinter import Tk, ttk, Frame
import PIL.Image, PIL.ImageTk
from iconos import Iconos
from Gui import FrameGenerico as fg
from datetime import datetime
from Entidades.Paciente import Paciente
from Entidades import Init

class PacienteGui(fg.FrameGenerico):
    def __init__(self, parent, cnf={}, **kw):
        fg.FrameGenerico.__init__(self, parent, cnf, **kw)
        self.session = Init.getSession()
        self.listaSexo=['Femenino','Masculino']
        self.registroNuevo=False
        self.offset=0
        self.cantidadRegistros = self.session.query(Paciente).count()

        panelPrincipal = self.getPanelPrincipal()
        Label(panelPrincipal,text="Nombre").grid(row=0,column=0)
        self.entradaNombre = Entry(panelPrincipal)
        self.entradaNombre.grid(row=0,column=1,columnspan=2,sticky=E+W)
        Label(panelPrincipal, text="Apellido").grid(row=0, column=3)
        self.entradaApellido = Entry(panelPrincipal)
        self.entradaApellido.grid(row=0, column=4)
        Label(panelPrincipal, text="Sexo").grid(row=0, column=5)
        self.comboBoxSexo = ttk.Combobox(panelPrincipal, values=self.listaSexo)
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

        self.checkBoxObraSocial=Checkbutton(panelPrincipal,text="Tiene obra social")
        self.checkBoxObraSocial.grid(row=2,column=2)

        Label(panelPrincipal, text="Obra social").grid(row=2, column=3)
        self.entradaObraSocial = Entry(panelPrincipal)
        self.entradaObraSocial.grid(row=2, column=4)

        Label(panelPrincipal, text="Nro afiliado").grid(row=2, column=5)
        self.entradaNroAfiliado = Entry(panelPrincipal)
        self.entradaNroAfiliado.grid(row=2, column=6)

        Label(panelPrincipal, text="Dirección").grid(row=3, column=0)
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

        Label(panelPrincipal, text="Evaluación").grid(row=10, column=0,sticky=W)
        self.textEvaluacion = Text(panelPrincipal,height=5)
        self.textEvaluacion.grid(row=11, column=0,columnspan=7,sticky=(N,E,S,W))

        Label(panelPrincipal, text="Evolución").grid(row=12, column=0,sticky=W)
        self.textEvolucion = Text(panelPrincipal,height=5)
        self.textEvolucion.grid(row=13, column=0,columnspan=7,sticky=(N,E,S,W))

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
        paciente = Paciente()
        paciente.pacienteNombre = self.entradaNombre.get()
        paciente.pacienteApellido = self.entradaApellido.get()
        self.session.add(paciente)
        self.session.commit()

    def getNext(self):
        super().getNext()
        self.clearForm()
        if self.offset > 0:
            self.offset += 1
        if self.registroNuevo:
            paciente = self.session.query(Paciente).order_by(Paciente.nombre.asc()).offset(self.offset).first()
            if paciente is not None:
                self.paciente = paciente
                self.copyToWindow()
        else:
            self.getLast()

    def getLast(self):
        super().getLast()
        self.clearForm()
        self.offset = self.cantidadRegistros - 1
        paciente = self.session.query(Paciente).order_by(Paciente.pacienteApellido.asc()).offset(self.offset).first()
        if paciente is not None:
            self.paciente = paciente
            self.copyToWindow()

    def borrar(self):
        super().borrar()

    def getFirst(self):
        super().getFirst()
        self.clearForm()
        self.paciente = self.session.query(Paciente).order_by(Paciente.pacienteApellido).first()
        self.copyToWindow()

    def getPrev(self):
        super().getPrev()
        self.clearForm()
        if self.offset > 0:
            self.offset -= 1
        if self.registroNuevo:
            paciente = self.session.query(Paciente).order_by(Paciente.pacienteNombre.asc()).offset(self.offset).first()
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

    def clearForm(self):
        super().clearForm()
        self.paciente = Paciente()
        self.registroNuevo = True
        self.offset = 0
        self.entradaNombre.insert(0, '')
        self.entradaApellido.insert(0, '')
        self.comboBoxSexo.set('')
        self.entradaNivelEducativo.insert(0, '')
        self.entradaFechaNacimiento.insert(0, '')
        self.entradaDocumento.insert(0, '')
        self.checkBoxObraSocial.deselect()
        self.entradaObraSocial.insert(0, '')
        self.entradaNroAfiliado.insert(0, '')
        self.entradaDireccion.insert(0, '')


if __name__ == '__main__':
    root = Tk()
    paciente = PacienteGui(root, width=507, height=358)
    paciente.pack()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    root.mainloop()


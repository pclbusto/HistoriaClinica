from sqlalchemy import Column, Integer, String, Boolean
from Entidades import Init

class Paciente(Init.Base):
    __tablename__='Pacientes'
    __table_args__ = {'sqlite_autoincrement': True}
    pacienteId = Column(Integer, primary_key=True)
    pacienteNombre = Column(String, default='')
    pacienteApellido = Column(String, default='')
    pacienteSexo = Column(Integer, default=-1)
    pacienteFechaNacimiento= Column(Integer, default=0)
    pacienteNivelEducativo = Column(String, default='')
    pacienteDocumento = Column(String, default='')
    pacienteTieneObraSocial = Column(Boolean, default=False)
    obraSocialNombre = Column(String, default='')
    pacienteNroAfiliado = Column(String, default='')
    pacienteDireccion = Column(String, default='')
    pacienteTelefono = Column(String, default='')
    pacienteMail = Column(String, default='')
    derivadoPor = Column(String, default='')
    motivoConsulta = Column(String, default='')
    antecedentes = Column(String, default='')

    def __repr__(self):
        return "<Paciente.py(pacienteId='%s',pacienteNombre='%s')>" %(self.pacienteId, self.pacienteNombre)




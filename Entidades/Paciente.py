from sqlalchemy import Column, Integer, String, Boolean
from Entidades import Init

class Paciente(Init.Base):
    __tablename__='Pacientes'
    __table_args__ = {'sqlite_autoincrement': True}
    pacienteId = Column(Integer, primary_key=True)
    pacienteNombre = Column(String)
    pacienteApellido = Column(String)
    pacienteFechaNacimiento= Column(Integer)
    pacienteNivelEducativo = Column(String)
    pacienteDocumento = Column(String)
    pacienteTieneObraSocial = Column(Boolean)
    obraSocialNombre = Column(String)
    pacienteNroAfiliado = Column(String)
    pacienteDireccion = Column(String)
    pacienteTelefono = Column(String)
    pacienteMail = Column(String)
    derivadoPor = Column(String)
    motivoConsulta = Column(String)

    def __repr__(self):
        return "<Paciente.py(pacienteId='%s',pacienteNombre='%s')>" %(self.pacienteId, self.pacienteNombre)



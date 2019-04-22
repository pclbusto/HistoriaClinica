from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Init import Base

class Paciente(Base):
    __tablename__='pacientes'
    __table_args__ = {'sqlite_autoincrement': True}
    paciente_id = Column(Integer, primary_key=True)
    paciente_nombre = Column(String, default='')
    paciente_apellido = Column(String, default='')
    paciente_sexo = Column(Integer, default=-1)
    paciente_fecha_nacimiento= Column(Integer, default=0)
    paciente_nivel_educativo = Column(String, default='')
    paciente_documento = Column(String, default='')
    paciente_obra_social = Column(Integer, ForeignKey('obra_sociales.obra_social_id'))
    paciente_nro_afiliado = Column(String, default='')
    paciente_direccion = Column(String, default='')
    paciente_telefono = Column(String, default='')
    paciente_mail = Column(String, default='')
    derivado_por = Column(String, default='')
    motivo_consulta = Column(String, default='')
    antecedentes = Column(String, default='')

    def __repr__(self):
        return "<Paciente.py(pacienteId='%s',pacienteNombre='%s')>" %(self.paciente_id, self.paciente_nombre)

class Obra_Social(Base):
    __tablename__='obra_sociales'
    __table_args__ = {'sqlite_autoincrement': True}
    obra_social_id = Column(Integer, primary_key=True)
    obra_social_nombre = Column(String, default='')
##    paciente_id = Column(Integer, ForeignKey('pacientes.paciente_id'))
    pacientes = relationship("Paciente")
    def __repr__(self):
        return "<obra social Id='%s',obra social nombre='%s')>" %(self.obra_social_id, self.obra_social_nombre)

class Profecional(Base):
    __tablename__='profecional'
    __table_args__ = {'sqlite_autoincrement': True}
    profecional_id = Column(Integer, primary_key=True)
    profecional_nombre = Column(String, default='')
    def __repr__(self):
        return "<profecional Id='%s',profecional nombre='%s')>" %(self.profecional_id, self.profecional_nombre)






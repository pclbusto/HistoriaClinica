from sqlalchemy import Column, Integer, String, Boolean
from Entidades import Init

class Nota(Init.Base):
    __tablename__='Notas'
    pacienteId = Column(Integer, primary_key=True)
    notaFecha = Column(Integer, default=0)
    notaTipoNota = Column(Integer, default=0)
    notaText = Column(String, default='')

    TIPO_NOTA_MOTIVO_CONSULTA = 1
    TIPO_NOTA_ANTECEDENTE = 2
    TIPO_NOTA_PROBLEMA_ACTUAL = 3
    TIPO_NOTA_AVALUACION = 4
    TIPO_NOTA_EVOLUCION = 5

    def __repr__(self):
        return "<nota.py(pacienteId='%s',notaFecha='%s')>" %(self.pacienteId, self.notaFecha)



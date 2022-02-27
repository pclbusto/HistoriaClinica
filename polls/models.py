from django.db import models


class Sexo(models.TextChoices):
    MASCULINO = 'M', _('Masculino')
    FEMENINO = 'F', _('Femenino')
    OTRO = 'O', _('Otro')

class Paciente(models.Model):
    documento_text = models.CharField("Documento", max_length=15)
    paciente_nombre_text = models.CharField("Nombre", max_length=150)
    paciente_apellido_text= models.CharField("Apellido", max_length=150)
    paciente_fecha_nacimiento_date = models.DateField('Fecha Nacimiento')
    paciente_sexo_enum = models.CharField("Sexo", max_length=1, choices=Sexo)




    #     paciente_nivel_educativo = Column(String, default='')
    #     paciente_documento = Column(String, default='')
    #     paciente_obra_social = Column(Integer, ForeignKey('obra_sociales.obra_social_id'))
    #     paciente_nro_afiliado = Column(String, default='')
    #     paciente_direccion = Column(String, default='')
    #     paciente_telefono = Column(String, default='')
    #     paciente_mail = Column(String, default='')
    #     derivado_por = Column(String, default='')
    #     motivo_consulta = Column(String, default='')
    #     antecedentes = Column(String, default='')
    #
    #     def __repr__(self):
    #         return "<Paciente.py(pacienteId='%s',pacienteNombre='%s')>" % (self.paciente_id, self.paciente_nombre)
    #
    # class Obra_Social(Base):
    #     __tablename__ = 'obra_sociales'
    #     __table_args__ = {'sqlite_autoincrement': True}
    #     obra_social_id = Column(Integer, primary_key=True)
    #     obra_social_nombre = Column(String, default='')
    #     ##    paciente_id = Column(Integer, ForeignKey('pacientes.paciente_id'))
    #     pacientes = relationship("Paciente")
    #
    #     def __repr__(self):
    #         return "<obra social Id='%s',obra social nombre='%s')>" % (self.obra_social_id, self.obra_social_nombre)
    #
    # class Profecional(Base):
    #     __tablename__ = 'profecional'
    #     __table_args__ = {'sqlite_autoincrement': True}
    #     profecional_id = Column(Integer, primary_key=True)
    #     profecional_nombre = Column(String, default='')
    #
    #     def __repr__(self):
    #         return "<profecional Id='%s',profecional nombre='%s')>" % (self.profecional_id, self.profecional_nombre)
    #


    def __str__(self):
        return "Documento: {}, Nombre: {}, Apellido: {}, Fecha Nacimiento: {}".format(self.documento_text, self.nombre_text, self.apellido_text, self.fecha_nacimiento_date)


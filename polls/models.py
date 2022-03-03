from django.db import models
from datetime import date

class Obra_Social(models.Model):
    obra_social_nombre_text = models.CharField("Nombre", max_length=50, default='')
    obra_social_descripcion_text = models.CharField("Nombre", max_length=150, default='')
    verbose_name = "Obra Social"
    verbose_name_plural = "Obra Sociales"
    def __str__(self):
        return self.obra_social_nombre_text

class Paciente(models.Model):
    Sexo = [(' ', ' '), ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]
    Nivel_Educativo = [('',''), ('Primario','Primario'), ('Secundario','Secundario'), ('Terciario','Terciario'), ('Universitario','Universitario')]

    paciente_documento_text = models.CharField("Documentos", max_length=15)
    paciente_nombre_text = models.CharField("Nombre", max_length=150, default='')
    paciente_apellido_text= models.CharField("Apellido", max_length=150, default='')
    paciente_fecha_nacimiento_date = models.DateField('Fecha Nacimiento', default=date.today())
    paciente_sexo_enum = models.CharField("Sexo", max_length=1, choices=Sexo, default=' ')
    paciente_nivel_educativo_enum = models.CharField("Nivel Educativo", max_length=15, choices=Nivel_Educativo, default=' ')
    paciente_obra_social = models.ForeignKey(Obra_Social, on_delete= models.DO_NOTHING)
    paciente_nro_afiliado_text = models.CharField("Nro Afiliado", max_length=15, default='')
    paciente_direccion_text = models.CharField("Nro Afiliado", max_length=25, default='')
    paciente_telefono_text = models.CharField("Telefono",  max_length=25, default='')
    paciente_mail_text = models.CharField("Correo Electronico", max_length=125, default='')

    def __str__(self):
        return "Documento: {}, Nombre: {}, Apellido: {}, Fecha Nacimiento: {}".format(self.paciente_documento_text, self.paciente_nombre_text, self.paciente_apellido_text, self.paciente_fecha_nacimiento_date)


    #     derivado_por = Column(String, default='')
    #     motivo_consulta = Column(String, default='')
    #     antecedentes = Column(String, default='')

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



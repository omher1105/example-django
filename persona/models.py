from django.db import models


# Create your models here.
class PersonaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, null=True, blank=True, default=None)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    createAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

from django.db import models

class Meseros(models.Model):
    class Meta:
        verbose_name_plural = 'Meseros'

    nombre = models.CharField(max_length=254, blank=True, null=True)
    apellido = models.CharField(max_length=254, blank=True, null=True)
    dni = models.CharField(max_length=12, verbose_name='D.N.I.', blank=True, null=True)
    procedencia = models.CharField(max_length=254, blank=True, null=True)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}, {} (DNI: {})".format(self.apellido, self.nombre, self.dni or '-')
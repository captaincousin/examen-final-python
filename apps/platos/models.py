from django.db import models

class Platos(models.Model):
    class Meta:
        verbose_name_plural = 'Platos'

    nombre = models.CharField(max_length=254, blank=True, null=True)
    precio = models.PositiveIntegerField(default=0)
    procedencia = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.nombre, self.precio)

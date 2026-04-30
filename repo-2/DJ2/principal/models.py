from django.db import models

class Gasto(models.Model):
    # El 'id' lo crea Django automáticamente como clave primaria
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")
    fecha = models.DateField(verbose_name="Fecha del Gasto")

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
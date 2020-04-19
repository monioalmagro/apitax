from django.db import models
from django.utils.timezone import now

class Ingreso(models.Model):
    monto=models.CharField(verbose_name="monto" ,max_length=50)

    

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return self.name

    
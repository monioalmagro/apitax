from django.db import models
from django.utils.timezone import now

class Ingreso(models.Model):
    #monto=models.CharField(verbose_name="monto" ,max_length=50)
    monto=models.IntegerField(verbose_name="monto")
    descripcion=models.CharField(null=True,verbose_name="descripcion" ,max_length=200)
    fecha= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return self.name

    
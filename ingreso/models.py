from django.db import models
from django.utils.timezone import now

class Ingreso(models.Model):
    
    monto=models.IntegerField(verbose_name="monto")
    descripcion=models.CharField(verbose_name="descripcion" ,max_length=200)
    fecha= models.DateTimeField( verbose_name='Fecha de creación')
    

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return self.descripcion

class Cuenta(models.Model):
    cuenta=models.CharField(verbose_name="cuenta", max_length=50)
    categoria=models.CharField(verbose_name="categoria", max_length=50)
    signo=models.CharField(verbose_name="signo", max_length=3)

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return self.cuenta

class Movimiento(models.Model):
    cuenta =models.CharField(verbose_name="cuenta", max_length=50)
    #categoria=models.CharField(verbose_name="categoria", max_length=50)
    cantidad=models.IntegerField(verbose_name="cantidad")
    signo=models.CharField(verbose_name="signo", max_length=50)
    detalle=models.CharField(verbose_name="detalle", max_length=50,null=True, blank=True)
    fecha = models.DateTimeField(verbose_name="fecha", default = now)

    

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

    def __str__(self):
        return self.cuenta

        

   

   
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

class Categoria(models.Model):
    cuenta=models.CharField(verbose_name="cuenta", max_length=50)
    categoria=models.CharField(verbose_name="categoria", max_length=50)
    signo=models.CharField(verbose_name="signo", max_length=3)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria

class Movimiento(models.Model):
    cuenta =models.CharField("cuenta", max_length=50)
    #categoria=models.CharField(verbose_name="categoria", max_length=50)
    cantidad=models.IntegerField("cantidad")
    signo=models.CharField("signo", max_length=50)
    detalle=models.CharField("detalle", max_length=50)
    models.DateTimeField("fecha", auto_now=True, auto_now_add=True)

    

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

    def __str__(self):
        return self.movimiento

        

   

   
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30,unique=True)

class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    foto = models.FileField(upload_to=f"fotos/",null=True,blank=True)
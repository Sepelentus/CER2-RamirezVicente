from django.db import models

# Create your models here.
class Residencia(models.Model):
    NRO = models.IntegerField(primary_key=True)
    Owner = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Mail = models.CharField(max_length=70)

class Conserje(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Fono = models.IntegerField()

class Correspondencia(models.Model):
    Fecha_recepcion = models.DateField(null=True, blank=True)
    conserje = models.ForeignKey(Conserje, on_delete=models.CASCADE)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estados = [
        ('Buen estado', 'Buen estado'),
        ('Poco dañado', 'Poco dañado'),
        ('Mal estado','Mal estado'),
    ]
    Estado = models.CharField(max_length=15,
        choices=estados,
        default='Buen estado')
    NroResidencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    

from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
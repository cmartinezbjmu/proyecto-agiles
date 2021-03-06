from django.db import models
from .etiqueta import Etiqueta
from .tipo import Tipo
from datetime import datetime

# Create your models here.
class Recurso(models.Model):
    FASE_TYPES = (
        ('A', 'Pre-Producción'),
        ('B', 'Producción'),
        ('C', 'Pos-Producción'),
        ('D', 'Control calidad'),
        ('E', 'Cierre proyecto'),
        ('F', 'Sistematización y resguardo')
    )
    nombre = models.CharField(max_length=200)
    proyecto = models.CharField(max_length=200)
    fase = models.CharField(max_length=1, choices=FASE_TYPES)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    inicio_produccion = models.DateField(blank=True, null=True, default=datetime.now)
    fin_elaboracion_recurso = models.DateField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "recurso"
        verbose_name_plural = "recursos"
        ordering = ['-inicio_produccion']

    def etiquetas_list(self):
        return self.etiquetas.all()

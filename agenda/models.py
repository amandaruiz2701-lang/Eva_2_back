from django.db import models

# Create your models here.
class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, verbose_name='Nombre Clienta')
    fecha_cita = models.DateField(
        verbose_name='Fecha Cita (Ej: 2026-12-31)', 
        help_text='Formato requerido: AAAA-MM-DD (Año-Mes-Día)'
    )
    servicio = models.CharField(max_length=50, verbose_name='Servicio')
    estilista = models.CharField(max_length=50, verbose_name='Estilista')
    duracion_minutos = models.IntegerField(verbose_name='Duración (min)')
    costo = models.IntegerField(verbose_name='Costo ($)')
    estado = models.CharField(max_length=30, verbose_name='Estado')
    imagen_antes = models.ImageField(upload_to='imagenes/', verbose_name='Foto Antes / Referencia', null=True, blank=True)
    imagen_despues = models.ImageField(upload_to='imagenes/', verbose_name='Foto Después / Resultado', null=True, blank=True)
    observaciones = models.TextField(verbose_name='Fórmula y Observaciones', null=True, blank=True)

    def __str__(self):
        fila = 'Cliente: ' + self.nombre_cliente + ' - Servicio: ' + self.servicio
        return fila

    def delete(self, using=None, keep_parents=False):
        if self.imagen_antes:
            self.imagen_antes.storage.delete(self.imagen_antes.name)
        if self.imagen_despues:
            self.imagen_despues.storage.delete(self.imagen_despues.name)
        super().delete()
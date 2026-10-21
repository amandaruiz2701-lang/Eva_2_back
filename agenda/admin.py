from django.contrib import admin
from .models import Cita
# Register your models here.

class CitaAdmin(admin.ModelAdmin):
   list_display = ['id', 'nombre_cliente', 'fecha_cita', 'servicio', 'estilista', 'costo', 'estado']

admin.site.register(Cita, CitaAdmin)
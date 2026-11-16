from django.contrib import admin
from .models import Servicio, Cita

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    # Usa exactamente los mismos nombres que pusiste en models.py
    list_display = ('nombre', 'costo', 'duracion_minutos', 'estilista')  
    search_fields = ('nombre',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'servicio', 'fecha_cita', 'estado')
    list_filter = ('estado', 'fecha_cita')
    search_fields = ('cliente__username', 'servicio__nombre', 'estilista')
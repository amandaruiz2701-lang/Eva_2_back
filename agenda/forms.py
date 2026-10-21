from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

    def clean_costo(self):
        costo_ingresado = self.cleaned_data.get('costo')
        if costo_ingresado is not None and costo_ingresado <= 0:
            raise forms.ValidationError("El costo del servicio debe ser mayor a 0.")
        return costo_ingresado

    def clean_duracion_minutos(self):
        duracion = self.cleaned_data.get('duracion_minutos')
        if duracion is not None and (duracion < 10 or duracion > 480):
            raise forms.ValidationError("La duración debe estar entre 10 y 480 minutos.")
        return duracion
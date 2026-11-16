from django import forms
from django.contrib.auth.models import User
from .models import Cita

# Formulario para el Registro de Nuevos Clientes
class RegistroClienteForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa una contraseña'})
    )
    password_confirm = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite la contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        # La clienta solo interactúa con esto:
        fields = ['servicio', 'fecha_cita', 'imagen_antes', 'imagen_despues', 'observaciones']
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control rounded-3', 'type': 'date'}),
            'imagen_antes': forms.ClearableFileInput(attrs={'class': 'form-control rounded-3'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control rounded-3', 'rows': 3, 'placeholder': '¿Alguna preferencia, tono o detalle especial?'}),
        }

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
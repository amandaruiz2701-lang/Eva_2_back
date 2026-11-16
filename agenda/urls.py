from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas, name='citas'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('confirmar/<int:id>/', views.confirmar_cita, name='confirmar_cita'),
]
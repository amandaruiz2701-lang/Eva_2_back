from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('citas', views.citas, name='citas'),
    path('citas/crear', views.crear, name='crear'),
    path('citas/editar/<int:id>', views.editar, name='editar'),
    path('citas/eliminar/<int:id>', views.eliminar, name='eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
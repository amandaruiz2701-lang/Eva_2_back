from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from agenda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('registro/', views.registro, name='registro'),
    
    # Deriva las rutas de la app agenda
    path('citas/', include('agenda.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
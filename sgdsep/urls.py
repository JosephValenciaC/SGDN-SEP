"""
URL configuration for sgdsep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sgdsep import settings
from sgdsistem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('principal/', views.principal, name='principal'),

    # Nominas
    path('importar/', views.importar, name='importar'),
    path('Inmuebles/', views.Inmuebles_home, name='Inmuebles_home'),
    path('Inmueble/<int:task_id>', views.Detalle_inmueble, name='Detalle_inmueble'),
    path('convertir_csv_a_excel/', views.convertir_csv_a_excel, name='convertir_csv_a_excel'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
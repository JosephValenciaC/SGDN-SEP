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

    # Inmuebles
    path('importar/', views.importar, name='importar'),
    path('Inmuebles/', views.Inmuebles_home, name='Inmuebles_home'),
    path('Inmueble/<int:task_id>', views.Detalle_inmueble, name='Detalle_inmueble'),
    path('convertir_csv_a_excel/', views.convertir_csv_a_excel, name='convertir_csv_a_excel'),

    # Personas
    path('importar_personas/', views.importar_personas, name='importar_personas'),
    path('personas/', views.personas_home, name='personas_home'),
    path('persona/<int:persona_id>/', views.Detalle_persona, name='ver_persona'),

    # Nominas
    path('importar_nominas/', views.importar_nominas, name='importar_nominas'),
    path('nominas/', views.nominas_home, name='nominas_home'),
    path('nominas/<int:nomina_id>/', views.detalle_nomina, name='detalle_nomina'),
    path('generar_pdf/', views.generar_pdf_nominas, name='generar_pdf_nominas'),
    
    # Plazas
    path('importar_plazas/', views.importar_plazas, name='importar_plazas'),
    path('plazas/', views.plazas_home, name='plazas_home'),
    path('plazas/<int:plaza_id>/', views.detalle_plaza, name='detalle_plaza'),
    # path('generar_pdf/', views.generar_pdf_nominas, name='generar_pdf_nominas'),
    
    # Analitico
    path('importar_analitico/', views.importar_analitico, name='importar_analitico'),
    path('analitico/', views.analitico_home, name='analitico_home'),
    path('analitico/<int:analitico_id>/', views.detalle_analitico, name='detalle_analitico'),
    
      # MDP
    path('importar_mdp/', views.importar_mdp, name='importar_mdp'),
    path('mdp/', views.mdp_home, name='mdp_home'),
    path('mdp/<int:mdp_id>/', views.detalle_mdp, name='detalle_mdp'),
    
      # Lista Negra
    path('importar_lista_negra/', views.importar_lista_negra, name='importar_lista_negra'),
    path('lista_negra/', views.lista_negra_home, name='lista_negra_home'),
    path('lista_negra/<int:lista_negra_id>/', views.detalle_lista_negra, name='detalle_lista_negra'),
    
    # Consulta Global
    path('consulta_global/', views.consulta_global_home, name='consulta_global_home'),

    # Usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/crear/', views.create_user, name='create_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),


    # Configuracion
    path('configuracion/', views.configuracion_view, name='configuracion'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
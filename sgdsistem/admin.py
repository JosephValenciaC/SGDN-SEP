from django.contrib import admin
from .models import Inmuebles_data

# Define el modelo en el admin
class InmueblesDataAdmin(admin.ModelAdmin):
    list_display = ('CV_CCT', 'C_NOMBRE', 'CV_TIPO', 'estado')  # Campos que se mostrarán en la lista
    search_fields = ('CV_CCT', 'C_NOMBRE', 'CV_TIPO')  # Campos para búsqueda
    list_filter = ('estado', 'CV_TIPO')  # Filtros para las listas
    ordering = ('CV_CCT',)  # Ordenación por CV_CCT

# Registra el modelo en el admin
admin.site.register(Inmuebles_data, InmueblesDataAdmin)

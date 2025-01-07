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


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Obtén el modelo de usuario personalizado
CustomUser = get_user_model()

# Registra el modelo de usuario personalizado con una configuración personalizada, si es necesario.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Configura los campos que quieres que aparezcan en la lista y el formulario del admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Configura los formularios que se usarán para crear o editar usuarios
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),  # Agrega el campo `bio` si es parte de tu modelo `CustomUser`
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio',)}),  # Agrega el campo `bio` en el formulario de creación
    )

# Registra el modelo en el admin
admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from .models import NominasData

@admin.register(NominasData)
class NominasDataAdmin(admin.ModelAdmin):
    list_display = ('tipo_p', 'ud', 'municipio', 'localidad', 'ct', 'rfc', 'nombre', 'status_p', 'liquido')
    search_fields = ('rfc', 'nombre', 'ct', 'nss')
    list_filter = ('status_p', 'sexo', 'nivel_cm', 'qna_pago')
    ordering = ('-qna_pago', 'nombre')  # Ordenar por quincena de pago descendente y nombre ascendente}
    
    
    
    
from django.contrib import admin
from .models import PlazasData

@admin.register(PlazasData)
class PlazasDataAdmin(admin.ModelAdmin):
    list_display = (
        'rfc', 'ct', 'partida', 'unidad', 'subunidad', 
        'categoria', 'horas', 'plaza', 'nivel_cm', 
        'pzareq', 'nivel_pto', 'status_s', 'motivo_s',
        'desde_pla', 'hasta_pla', 'desde_pro', 'hasta_pro'
    )
    list_filter = (
        'status_s', 'unidad', 'subunidad', 'categoria', 
        'nivel_pto', 'desde_pla', 'desde_pro'
    )
    search_fields = (
        'rfc', 'ct', 'partida', 'plaza', 
        'status_s', 'motivo_s', 'unidad', 'subunidad'
    )
    ordering = ['rfc', 'desde_pla']
    list_per_page = 20


from django.contrib import admin
from .models import AnaliticoData

@admin.register(AnaliticoData)
class AnaliticoDataAdmin(admin.ModelAdmin):
    list_display = (
        'rfc', 'curp', 'ct', 'motivo', 'desde', 'hasta', 
        'zona_fone', 'ct_fone', 'nivel_ct', 'cve_clasificador', 
        'cve_plaza', 'cve_plaza_sin_esp', 'cve_plaza_fone', 
        'unid_subunid'
    )
    list_filter = (
        'motivo', 'zona_fone', 'nivel_ct', 'cve_clasificador', 
        'cve_plaza', 'desde', 'hasta'
    )
    search_fields = (
        'rfc', 'curp', 'ct', 'motivo', 'ct_fone', 
        'cve_plaza', 'cve_plaza_sin_esp', 'cve_plaza_fone', 
        'unid_subunid'
    )
    ordering = ['rfc', 'desde']
    list_per_page = 20


from django.contrib import admin
from .models import MDPData

@admin.register(MDPData)
class MDPDataAdmin(admin.ModelAdmin):
    # Campos para mostrar en la lista
    list_display = (
        'NUM', 
        'ENTIDAD_FEDERATIVA', 
        'curp', 
        'rfc', 
        'nombre', 
        'CODIGO_POSTAL', 
        'cve_plaza', 
        'ESTATUS_ACTUAL_DE_LA_PLAZA', 
        'MOVIMIENTO', 
        'FECHA_INICIAL', 
        'FECHA_FINAL'
    )
    
    # Campos clicables para acceder a los detalles
    list_display_links = ('NUM', 'curp', 'rfc', 'nombre')
    
    # Campos de búsqueda
    search_fields = ('curp', 'rfc', 'nombre', 'cve_plaza', 'MOVIMIENTO')
    
    # Filtros laterales
    list_filter = (
        'ENTIDAD_FEDERATIVA', 
        'ESTATUS_ACTUAL_DE_LA_PLAZA', 
        'ESTATUS_DEL_NOMBRAMIENTO', 
        'ALTA_VIGENTE', 
        'REGIMEN'
    )
    
    # Opciones de ordenación
    ordering = ('NUM', 'ENTIDAD_FEDERATIVA')
    
    # Campos de solo lectura (si es necesario proteger algunos)
    readonly_fields = ('FECHA_DE_REGISTRO',)
    
    # Configuración para editar campos agrupados
    fieldsets = (
        ('Información Personal', {
            'fields': ('curp', 'rfc', 'nombre', 'ENTIDAD_FEDERATIVA', 'CODIGO_POSTAL')
        }),
        ('Datos de Plaza', {
            'fields': ('cve_plaza', 'ESTATUS_ACTUAL_DE_LA_PLAZA', 'ESTATUS_DEL_NOMBRAMIENTO', 'REGIMEN')
        }),
        ('Detalles del Movimiento', {
            'fields': ('MOVIMIENTO', 'CODIGO_DEL_MOVIMIENTO', 'ALTA_VIGENTE', 'DESCRIPCION')
        }),
        ('Fechas', {
            'fields': ('FECHA_INICIAL', 'FECHA_FINAL', 'FECHA_DE_BAJA', 'FECHA_DE_REGISTRO')
        }),
        ('Otros', {
            'fields': ('NUM_DE_TICKET_MAI', 'FOLIO_REGISTRO_EXCEPCION', 'REGISTRO_EXTEMPORANEO')
        }),
    )

from django.contrib import admin
from .models import ListaNegraData

class ListaNegraDataAdmin(admin.ModelAdmin):
    list_display = ('sec', 'tipo', 'concepto', 'ct', 'rfc', 'curp', 'nombre', 'cve_plaza', 'desde', 'hasta', 'motivo', 'dup', 'usuario')

    list_filter = ('tipo', 'concepto', 'desde', 'hasta')

    search_fields = ('rfc', 'curp', 'nombre')

    list_per_page = 10
    ordering = ('sec',)
    fieldsets = (
        (None, {
            'fields': ('sec', 'tipo', 'concepto', 'ct', 'rfc', 'curp', 'nombre', 'cve_plaza')
        }),
        ('Fechas', {
            'fields': ('desde', 'hasta')
        }),
        ('Detalles', {
            'fields': ('motivo', 'dup', 'usuario')
        }),
    )

    # Incluir campos adicionales de información si es necesario (puedes personalizar esta sección)
    readonly_fields = ('sec',)

# Registrar el modelo y su administrador
admin.site.register(ListaNegraData, ListaNegraDataAdmin)


from django.contrib import admin
from .models import PersonasData

@admin.register(PersonasData)
class PersonasDataAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista del panel de administración
    list_display = (
        'idpersona', 
        'nombre', 
        'nombres', 
        'apell_pat', 
        'apell_mat', 
        'rfc', 
        'curp', 
        'sexo', 
        'nss', 
        'clabe'
    )
    
    # Campos por los que se puede buscar
    search_fields = ('idpersona', 'rfc', 'curp', 'nombre', 'nombres', 'apell_pat', 'apell_mat', 'nss')
    
    # Filtros disponibles en el panel de administración
    list_filter = ('sexo',)

    # Opciones de ordenación inicial
    ordering = ('idpersona',)

    # Configuración de visualización detallada
    fieldsets = (
        ("Información Personal", {
            'fields': ('idpersona', 'nombres', 'apell_pat', 'apell_mat', 'nombre', 'sexo')
        }),
        ("Documentación", {
            'fields': ('rfc', 'curp', 'nss', 'clabe')
        }),
        ("Datos de Ingreso", {
            'fields': ('ing_gob', 'ing_sep', 'ing_rama')
        }),
    )

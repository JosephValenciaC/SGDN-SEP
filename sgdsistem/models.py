from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Inmuebles_data(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_inmueble')
    CV_CCT = models.CharField(max_length=100, blank=True, null=True)
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Baja', 'Baja'),
        ('Completado', 'Completado'),
    ]
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='Activo', null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    PRIORIDAD_CHOICES = [('Alta', 'Alta'), ('Media', 'Media'),('Baja', 'Baja') ]
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Media', null=True, blank=True)
    creado = models.CharField(max_length=20,null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Nuevos campos para la sección de Ubicación
    fotografia_de_la_ubicacion = models.ImageField(upload_to='ubicacion_photos/', blank=True, null=True)
    C_NOMBRE = models.CharField(max_length=100, blank=True, null=True)
    CV_TIPO = models.CharField(max_length=100, blank=True, null=True)
    C_TIPO = models.CharField(max_length=100, blank=True, null=True)
    CV_ADMINISTRATIVA = models.CharField(max_length=100, blank=True, null=True)
    C_ADMINISTRATIVA = models.CharField(max_length=100, blank=True, null=True)
    CV_ESTATUS = models.CharField(max_length=10, blank=True, null=True)
    C_ESTATUS_CHOICE = [
        ('ACTIVO', 'ACTIVO'),
        ('INACTIVO', 'INACTIVO'),
        # Otras opciones para países si las necesitas
    ]
    C_ESTATUS  = models.CharField(max_length=10, choices=C_ESTATUS_CHOICE, default=' ', null=True, blank=True)
    F_FUNDACION = models.CharField(max_length=15, blank=True, null=True)
    ALTA_SISTEMA = models.CharField(max_length=15, blank=True, null=True)
    CAMBIO = models.CharField(max_length=15, blank=True, null=True)
    CLAUSURA = models.CharField(max_length=15, blank=True, null=True)
    REAPERTURA = models.CharField(max_length=15, blank=True, null=True)
    REAPERTURA_CON_CAMBIO = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_INMUEBLE = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_VIALIDAD_PRINCIPAL = models.CharField(max_length=150, blank=True, null=True)
    INMUEBLE_C_VIALIDAD_DERECHA = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_VIALIDAD_IZQUIERDA = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_VIALIDAD_POSTERIOR = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_N_EXTNUM = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_EXTALF = models.CharField(max_length=50, blank=True, null=True)
    INMUEBLE_N_INTNUM = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_INTALF = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_ENT = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_NOM_ENT = models.CharField(max_length=50, blank=True, null=True)
    INMUEBLE_CV_MUN = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_NOM_MUN = models.CharField(max_length=15, blank=True, null=True)
    Zona_Economica = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_LOC = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_NOM_LOC = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_AMBITO = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_NOM_AMBITO = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_ASEN = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_NOM_ASEN = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_TIPO_ASEN = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_TIPO_ASEN = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_CV_CODIGO_POSTAL = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_C_DESC_UBICACION = models.CharField(max_length=350, blank=True, null=True)
    INMUEBLE_LATITUD = models.CharField(max_length=15, blank=True, null=True)
    INMUEBLE_LONGITUD = models.CharField(max_length=15, blank=True, null=True)
    SOSTENIMIENTO_CV_CONTROL = models.CharField(max_length=15, blank=True, null=True)
    SOSTENIMIENTO_C_CONTROL = models.CharField(max_length=15, blank=True, null=True)
    SOSTENIMIENTO_CV_SUBCONTROL = models.CharField(max_length=15, blank=True, null=True)
    SOSTENIMIENTO_C_SUBCONTROL = models.CharField(max_length=15, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN1 = models.CharField(max_length=3, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN1 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN2 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN2 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN3 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN3 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN4 = models.CharField(max_length=150, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN4 = models.CharField(max_length=150, blank=True, null=True)
    DEPOPERATIVA_CV_DEPENDENCIAN5 = models.CharField(max_length=150, blank=True, null=True)
    DEPOPERATIVA_C_DEPENDENCIAN5 = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_CV_CARGO = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_CARGO = models.CharField(max_length=150, blank=True, null=True)
    CONTACTO_CV_TIPODIRECTOR = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_TIPODIRECTOR = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_ASOCIACION = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_CURP = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_RFC = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_NOMBRE  = models.CharField(max_length=150, blank=True, null=True)
    CONTACTO_C_APELLIDO1 = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_APELLIDO2 = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_TELEFONO = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_CELULAR = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_EMAIL = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_EXTENSION = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_PWEB = models.CharField(max_length=150, blank=True, null=True)
    SUPERVISION_CV_CCT = models.CharField(max_length=150, blank=True, null=True)
    JEFSEC_CV_CCT = models.CharField(max_length=50, blank=True, null=True)
    SERREG_CV_CCT = models.CharField(max_length=15, blank=True, null=True)
    INSTITUCION_PLANTEL = models.CharField(max_length=15, blank=True, null=True)
    C_TURNO_1 = models.CharField(max_length=15, blank=True, null=True)
    C_TURNO_2 = models.CharField(max_length=15, blank=True, null=True)
    C_TURNO_3 = models.CharField(max_length=15, blank=True, null=True)
    TIPONIVELSUB_CV_SERVICION1 = models.CharField(max_length=15, blank=True, null=True)
    TIPONIVELSUB_C_SERVICION1 = models.CharField(max_length=15, blank=True, null=True)
    TIPONIVELSUB_CV_SERVICION2 = models.CharField(max_length=15, blank=True, null=True)
    TIPONIVELSUB_C_SERVICION2 = models.CharField(max_length=50, blank=True, null=True)
    TIPONIVELSUB_CV_SERVICION3 = models.CharField(max_length=15, blank=True, null=True)
    TIPONIVELSUB_C_SERVICION3 = models.CharField(max_length=15, blank=True, null=True)
    C_SERVICIO_CAM = models.CharField(max_length=15, blank=True, null=True)
    CARACTERISTCA_CV_CARACTERIZAN1 = models.CharField(max_length=60, blank=True, null=True)
    CARACTERISTCA_C_CARACTERIZAN1 = models.CharField(max_length=25, blank=True, null=True)
    CARACTERISTCA_CV_CARACTERIZAN2 = models.CharField(max_length=15, blank=True, null=True)
    CARACTERISTCA_C_CARACTERIZAN2  = models.CharField(max_length=15, blank=True, null=True)
    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"
        permissions = [
            ('add_tasks_inmueble', 'Can add inmueble in tasks app'),
            ('change_tasks_inmueble', 'Can change inmueble in tasks app'),
            ('delete_tasks_inmueble', 'Can delete inmueble in tasks app'),
            ('view_tasks_inmueble', 'Can view inmueble in tasks app'),
        ]


    
# class Nominas_data(models.Model):
#     assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_inmueble')
#     ESTADO_CHOICES = [
#         ('Activo', 'Activo'),
#         ('Baja', 'Baja'),
#         ('Completado', 'Completado'),
#     ]   
#     estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='Activo', null=True, blank=True)
#     creado = models.CharField(max_length=20,null=True, blank=True)
#     updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     tipo_p = models.CharField(max_length=2, blank=True, null=True)
#     ud = models.CharField(max_length=5, blank=True, null=True)
#     municipio = models.CharField(max_length=5, blank=True, null=True)
#     localidad  = models.CharField(max_length=5, blank=True, null=True)
#     ct = models.CharField(max_length=12, blank=True, null=True)
#     zonaesc = models.CharField(max_length=5, blank=True, null=True)
#     zona = models.CharField(max_length=2, blank=True, null=True)
#     prog = models.CharField(max_length=2, blank=True, null=True)
#     sub_prog = models.CharField(max_length=2, blank=True, null=True)
#     proyec = models.CharField(max_length=12, blank=True, null=True)
#     nss = models.CharField(max_length=12, blank=True, null=True)
#     rfc = models.CharField(max_length=13, blank=True, null=True)
#     curp = models.CharField(max_length=18, blank=True, null=True)
#     nombre = models.CharField(max_length=60, blank=True, null=True)
#     fech_ing = models.CharField(max_length=5, blank=True, null=True)
#     SEXO_CHOICE= [
#         ('F', 'F'),
#         ('M', 'M'),
#     ]   
#     sexo =  models.CharField(max_length=1, choices=SEXO_CHOICE, default='', null=True, blank=True)
#     cve_plaza = models.CharField(max_length=22, blank=True, null=True)
#     nivel_cm = models.CharField(max_length=3, blank=True, null=True)
#     status_p = models.CharField(max_length=3, blank=True, null=True)
#     mot_pla = models.CharField(max_length=3, blank=True, null=True)
#     num_cheq = models.CharField(max_length=3, blank=True, null=True)
#     qna_pago = models.CharField(max_length=3, blank=True, null=True)
#     p_desde = models.CharField(max_length=3, blank=True, null=True)
#     p_hasta = models.CharField(max_length=3, blank=True, null=True)
#     liquido = models.CharField(max_length=10, blank=True, null=True)
#     comodin = models.CharField(max_length=2, blank=True, null=True)
#     trailers = models.CharField(max_length=3, blank=True, null=True)
#     c01 = models.CharField(max_length=3, blank=True, null=True)
#     t01 = models.CharField(max_length=3, blank=True, null=True)
#     i01 = models.CharField(max_length=3, blank=True, null=True)
#     d01 = models.CharField(max_length=5, blank=True, null=True)
#     h01 = models.CharField(max_length=4, blank=True, null=True)
#     c02 = models.CharField(max_length=4, blank=True, null=True)
#     t02 = models.CharField(max_length=2, blank=True, null=True)
#     i02 = models.CharField(max_length=10, blank=True, null=True)
#     d02 = models.CharField(max_length=4, blank=True, null=True)
#     h02 = models.CharField(max_length=4, blank=True, null=True)
#     c03 = models.CharField(max_length=2, blank=True, null=True)
#     t03 = models.CharField(max_length=2, blank=True, null=True)
#     i03 = models.CharField(max_length=10, blank=True, null=True)
#     d03 = models.CharField(max_length=4, blank=True, null=True)
#     h03 = models.CharField(max_length=4, blank=True, null=True)






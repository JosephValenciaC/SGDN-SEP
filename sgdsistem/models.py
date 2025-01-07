from django.db import models
from django.conf import settings



class Inmuebles_data(models.Model):
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Cambia a AUTH_USER_MODEL para soportar CustomUser
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_inmueble',
    )
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
    INMUEBLE_C_VIALIDAD_PRINCIPAL = models.CharField(max_length=50, blank=True, null=True)
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
    SOSTENIMIENTO_C_DEPENDENCIAN1 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN2 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN2 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN3 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN3 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_CV_DEPENDENCIAN4 = models.CharField(max_length=50, blank=True, null=True)
    SOSTENIMIENTO_C_DEPENDENCIAN4 = models.CharField(max_length=50, blank=True, null=True)
    DEPOPERATIVA_CV_DEPENDENCIAN5 = models.CharField(max_length=50, blank=True, null=True)
    DEPOPERATIVA_C_DEPENDENCIAN5 = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_CV_CARGO = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_CARGO = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_CV_TIPODIRECTOR = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_TIPODIRECTOR = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_ASOCIACION = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_CURP = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_RFC = models.CharField(max_length=15, blank=True, null=True)
    CONTACTO_C_NOMBRE  = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_APELLIDO1 = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_APELLIDO2 = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_TELEFONO = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_CELULAR = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_EMAIL = models.CharField(max_length=50, blank=True, null=True)
    CONTACTO_C_EXTENSION = models.CharField(max_length=10, blank=True, null=True)
    CONTACTO_C_PWEB = models.CharField(max_length=50, blank=True, null=True)
    SUPERVISION_CV_CCT = models.CharField(max_length=50, blank=True, null=True)
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
            ('administrar_Inmueble', 'Puede administrar los inmuebles'),
        ]


    

# ---------------------------PERSONAS--------------------------------------------------
class PersonasData(models.Model):
    idpersona = models.CharField(max_length=10, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True)  # CURP tiene 18 caracteres
    nombres = models.CharField(max_length=150, blank=True, null=True)
    apell_pat = models.CharField(max_length=100, blank=True, null=True)  # Apellido paterno
    apell_mat = models.CharField(max_length=100, blank=True, null=True)  # Apellido materno
    nombre = models.CharField(max_length=100, blank=True, null=True)  # Nombre completo
    sexo = models.CharField(max_length=10, blank=True, null=True)
    nss = models.CharField(max_length=11, blank=True, null=True)  # El NSS tiene 11 caracteres
    clabe = models.CharField(max_length=26, blank=True, null=True)  # CLABE tiene 16 dígitos
    ing_gob = models.CharField(max_length=10, blank=True, null=True)
    ing_sep = models.CharField(max_length=10, blank=True, null=True)
    ing_rama = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} ({self.idpersona})"




# sgdsistem/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    PUESTO_CHOICES = [
        ('Capturista', 'Capturista'),
        ('Director', 'Director'),
        ('Usuario', 'Usuario'),
    ]
    puesto = models.CharField(max_length=50, choices=PUESTO_CHOICES, default='Usuario', blank=True, null=True)


    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Cambiar el related_name para evitar conflictos
        blank=True,
        help_text="Grupos a los que pertenece el usuario.",
        verbose_name="grupos",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Cambiar el related_name para evitar conflictos
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="permisos de usuario",
    )

    def __str__(self):
        return self.username


# ------------------------------ Nominas--------------------------------------

from django.db import models

class NominasData(models.Model):
    tipo_p = models.CharField(max_length=2, blank=True, null=True)
    ud = models.CharField(max_length=5, blank=True, null=True)
    municipio = models.CharField(max_length=5, blank=True, null=True)
    localidad = models.CharField(max_length=5, blank=True, null=True)
    ct = models.CharField(max_length=12, blank=True, null=True)
    zonaesc = models.CharField(max_length=5, blank=True, null=True)
    zona = models.CharField(max_length=5, blank=True, null=True)
    prog = models.CharField(max_length=5, blank=True, null=True)
    sub_prog = models.CharField(max_length=5, blank=True, null=True)
    proyec = models.CharField(max_length=5, blank=True, null=True)
    nss = models.CharField(max_length=11, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fech_ing = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    cve_plaza = models.CharField(max_length=22, blank=True, null=True)
    nivel_cm = models.CharField(max_length=5, blank=True, null=True)
    status_p = models.CharField(max_length=2, blank=True, null=True)
    mot_pla = models.CharField(max_length=5, blank=True, null=True) #Motivo
    num_cheq = models.CharField(max_length=10, blank=True, null=True)
    qna_pago = models.CharField(max_length=7, blank=True, null=True)
    p_desde = models.CharField(max_length=4, blank=True, null=True)
    p_hasta = models.CharField(max_length=4, blank=True, null=True)
    liquido = models.CharField(max_length=12, blank=True, null=True)
    comodin = models.CharField(max_length=2, blank=True, null=True)
    trailers = models.CharField(max_length=4, blank=True, null=True)
    clabe = models.CharField(max_length=24, blank=True, null=True)
    fuente = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Nómina {self.tipo_p} - {self.rfc}"

    class Meta:
        verbose_name = "Nómina"
        verbose_name_plural = "Nóminas"

# ------------------------------ PLAZAS ----------------------------------------
from django.db import models

class PlazasData(models.Model):
    rfc = models.CharField(max_length=13, blank=True, null=True)
    ct = models.CharField(max_length=12, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True) 
    partida = models.CharField(max_length=5, blank=True, null=True)
    unidad = models.CharField(max_length=4, blank=True, null=True)
    subunidad = models.CharField(max_length=4, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    horas = models.IntegerField()
    plaza = models.CharField(max_length=10, blank=True, null=True)
    nivel_cm = models.CharField(max_length=4, blank=True, null=True)
    pzareq = models.CharField(max_length=5, blank=True, null=True)
    nivel_pto = models.CharField(max_length=40, blank=True, null=True)
    docto_pla = models.CharField(max_length=40, blank=True, null=True)
    desde_pla = models.CharField(max_length=4, blank=True, null=True)
    hasta_pla = models.CharField(max_length=4, blank=True, null=True)
    docto_pro = models.CharField(max_length=10, blank=True, null=True)
    desde_pro = models.CharField(max_length=4, blank=True, null=True)
    hasta_pro = models.CharField(max_length=4, blank=True, null=True)
    status_s = models.CharField(max_length=2, blank=True, null=True)
    motivo_s = models.CharField(max_length=2, blank=True, null=True) #Motivo
    docto_s = models.CharField(max_length=40, blank=True, null=True)
    desde_s = models.CharField(max_length=4, blank=True, null=True)
    hasta_s = models.CharField(max_length=4, blank=True, null=True)
    tipmov_s = models.CharField(max_length=2, blank=True, null=True)
    situacion = models.CharField(max_length=10, blank=True, null=True)
    trailers = models.CharField(max_length=2, blank=True, null=True)
    cve_plaza = models.CharField(max_length=30, blank=True, null=True)
    idfone = models.CharField(max_length=10, blank=True, null=True)
    spd = models.CharField(max_length=20, blank=True, null=True)
    rfc_ok = models.CharField(max_length=15, blank=True, null=True)
    normalista = models.CharField(max_length=50, blank=True, null=True)
    plazafone = models.CharField(max_length=28, blank=True, null=True)

    def __str__(self):
        return f"{self.rfc} - {self.plaza}"

    class Meta:
        verbose_name = "Plaza Data"
        verbose_name_plural = "Plaza Data"




#------------------------------- MDP --------------------------------------
from django.db import models

class MDPData(models.Model):
    NUM = models.IntegerField(null=True, blank=True)
    ENTIDAD_FEDERATIVA = models.CharField(max_length=100, null=True, blank=True)
    curp = models.CharField(max_length=18, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    CODIGO_POSTAL = models.CharField(max_length=5, null=True, blank=True)
    cve_plaza = models.CharField(max_length=50, null=True, blank=True)
    ESTATUS_ACTUAL_DE_LA_PLAZA = models.CharField(max_length=2, null=True, blank=True)
    ESTATUS_DEL_NOMBRAMIENTO = models.CharField(max_length=50, null=True, blank=True)
    MOVIMIENTO = models.CharField(max_length=40, null=True, blank=True)
    CODIGO_DEL_MOVIMIENTO = models.CharField(max_length=10, null=True, blank=True)
    ALTA_VIGENTE = models.CharField(max_length=2, null=True, blank=True)
    DESCRIPCION = models.TextField( null=True, blank=True)
    FECHA_INICIAL = models.CharField(max_length=11, null=True, blank=True)
    FECHA_FINAL = models.CharField(max_length=10, null=True, blank=True)
    FECHA_DE_BAJA = models.CharField(max_length=10, null=True, blank=True)
    REGIMEN = models.CharField(max_length=50, null=True, blank=True)
    NUM_DE_TICKET_MAI = models.CharField(max_length=50, null=True, blank=True)
    FOLIO_REGISTRO_EXCEPCION = models.CharField(max_length=50, null=True, blank=True)
    REGISTRO_EXTEMPORANEO = models.CharField(max_length=10, null=True, blank=True)
    FECHA_DE_REGISTRO = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "MDP"
        verbose_name_plural = "MDP Data"

    def __str__(self):
        return f"{self.NUM} - {self.nombre}"



from django.db import models

# ------------------------------------- Analitico ----------------------
class AnaliticoData(models.Model):
    llave = models.CharField(max_length=50, null=True, blank=True)
    reporte_pago_2421 = models.CharField(max_length=50, null=True, blank=True)
    num = models.CharField(max_length=10, null=True, blank=True)
    ct = models.CharField(max_length=24, null=True, blank=True)
    zona_fone = models.CharField(max_length=2, null=True, blank=True)
    ct_fone = models.CharField(max_length=20, null=True, blank=True)
    nivel_ct = models.CharField(max_length=5, null=True, blank=True)
    cve_clasificador = models.CharField(max_length=2, null=True, blank=True)
    cve_plaza = models.CharField(max_length=25, null=True, blank=True)
    cve_plaza_sin_esp = models.CharField(max_length=25, null=True, blank=True)
    cve_plaza_fone = models.CharField(max_length=25, null=True, blank=True)
    unid_subunid = models.CharField(max_length=4, null=True, blank=True)
    nivel_educ = models.CharField(max_length=20, null=True, blank=True)
    fecha_crea = models.CharField(max_length=4, null=True, blank=True)
    categoria = models.CharField(max_length=10, null=True, blank=True)
    base_conf = models.CharField(max_length=2, null=True, blank=True)
    usicamm = models.CharField(max_length=10, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    nivel_pto = models.CharField(max_length=10, null=True, blank=True)
    tipo_plaza = models.CharField(max_length=2, null=True, blank=True)
    plazas = models.CharField(max_length=4, null=True, blank=True)
    horas = models.CharField(max_length=5, null=True, blank=True)
    hrs = models.CharField(max_length=5, null=True, blank=True)
    modelo = models.CharField(max_length=2, null=True, blank=True)
    fortalecim = models.CharField(max_length=50, null=True, blank=True)
    directivas = models.CharField(max_length=5, null=True, blank=True)
    programa = models.CharField(max_length=50, null=True, blank=True)
    sub_prog = models.CharField(max_length=50, null=True, blank=True)
    nivel_cm = models.CharField(max_length=4, null=True, blank=True)
    zona_eco = models.CharField(max_length=2, null=True, blank=True)
    zonas_iguales = models.CharField(max_length=20, null=True, blank=True)
    desde_s = models.CharField(max_length=4, null=True, blank=True)
    hasta_s = models.CharField(max_length=4, null=True, blank=True)
    status_s = models.CharField(max_length=2, null=True, blank=True)
    motivo_s = models.CharField(max_length=4, null=True, blank=True)
    status = models.CharField(max_length=2, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    en_lic_des = models.CharField(max_length=4, null=True, blank=True)
    reanuda_en = models.CharField(max_length=4, null=True, blank=True)
    resguardo = models.CharField(max_length=20, null=True, blank=True)
    docto_resg = models.TextField(null=True, blank=True)
    docto_resg_v2 = models.CharField(max_length=100, null=True, blank=True)
    motivo = models.CharField(max_length=4, null=True, blank=True)
    desde = models.CharField(max_length=4, null=True, blank=True)
    hasta = models.CharField(max_length=4, null=True, blank=True)
    rfc = models.CharField(max_length=13, null=True, blank=True)
    curp = models.CharField(max_length=18, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    paterno = models.CharField(max_length=100, null=True, blank=True)
    materno = models.CharField(max_length=100, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    cve_estado_civil = models.CharField(max_length=5, null=True, blank=True)
    ingreso_gob = models.CharField(max_length=4, null=True, blank=True)
    ingreso_sep = models.CharField(max_length=4, null=True, blank=True)
    ingreso_rama = models.CharField(max_length=4, null=True, blank=True)
    nss = models.CharField(max_length=15, null=True, blank=True)
    cve_estudio = models.CharField(max_length=4, null=True, blank=True)
    cp_fernando = models.CharField(max_length=50, null=True, blank=True)
    centro = models.CharField(max_length=18, null=True, blank=True)
    canc = models.CharField(max_length=4, null=True, blank=True)
    vac = models.CharField(max_length=4, null=True, blank=True)
    lic10 = models.CharField(max_length=4, null=True, blank=True)
    lic07 = models.CharField(max_length=4, null=True, blank=True)
    lic11 = models.CharField(max_length=4, null=True, blank=True)
    trece = models.CharField(max_length=4, null=True, blank=True)
    quince = models.CharField(max_length=4, null=True, blank=True)
    resg = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return f"{self.llave} - {self.nombre}"

    class Meta:
        verbose_name = "Analitico Data"
        verbose_name_plural = "Analitico Data"


# ------------------------ Lista Negra ------------------------------
class ListaNegraData(models.Model):
    sec = models.IntegerField(null=True, blank=True, verbose_name="Sec")
    tipo = models.CharField(max_length=2, null=True, blank=True, verbose_name="Tipo")
    concepto = models.CharField(max_length=5, null=True, blank=True, verbose_name="Concepto")
    ct = models.CharField(max_length=20, null=True, blank=True, verbose_name="Centro de Trabajo")
    rfc = models.CharField(max_length=13, null=True, blank=True, verbose_name="RFC")
    curp = models.CharField(max_length=18, null=True, blank=True, verbose_name="CURP")
    nombre = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombre")
    cve_plaza = models.CharField(max_length=50, null=True, blank=True, verbose_name="Clave de Plaza")
    desde = models.CharField(max_length=4, null=True, blank=True, verbose_name="Fecha Desde")
    hasta = models.CharField(max_length=4 ,null=True, blank=True, verbose_name="Fecha Hasta")
    motivo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Motivo")
    dup = models.CharField(max_length=2, default=False, verbose_name="Dup")
    usuario = models.CharField(max_length=100, null=True, blank=True, verbose_name="Usuario")

    def __str__(self):
        return f"{self.rfc} - {self.nombre}"

    class Meta:
        verbose_name = "Lista Negra"
        verbose_name_plural = "Listas Negras"
        ordering = ["-desde"]

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import AnaliticoData, Inmuebles_data, CustomUser, ListaNegraData, MDPData, NominasData, PersonasData, PlazasData

class InmueblesResource(resources.ModelResource):
    class Meta:
        model = Inmuebles_data
        fields = ('id', 'CV_CCT', 'estado', 'deadline', 'prioridad',
                  'creado', 'datecompleted', 'fotografia_de_la_ubicacion',
                  'C_NOMBRE', 'CV_TIPO', 'C_TIPO', 'CV_ADMINISTRATIVA', 'C_ADMINISTRATIVA',
                  'CV_ESTATUS', 'C_ESTATUS', 'F_FUNDACION', 'ALTA_SISTEMA', 'CAMBIO', 'CLAUSURA',
                  'REAPERTURA', 'REAPERTURA_CON_CAMBIO', 'INMUEBLE_CV_INMUEBLE', 'INMUEBLE_C_VIALIDAD_PRINCIPAL',
                  'INMUEBLE_C_VIALIDAD_DERECHA', 'INMUEBLE_C_VIALIDAD_IZQUIERDA', 'INMUEBLE_C_VIALIDAD_POSTERIOR',
                  'INMUEBLE_N_EXTNUM', 'INMUEBLE_C_EXTALF', 'INMUEBLE_N_INTNUM', 'INMUEBLE_C_INTALF',
                  'INMUEBLE_CV_ENT', 'INMUEBLE_C_NOM_ENT', 'INMUEBLE_CV_MUN', 'INMUEBLE_C_NOM_MUN',
                  'Zona_Economica', 'INMUEBLE_CV_LOC', 'INMUEBLE_C_NOM_LOC', 'INMUEBLE_CV_AMBITO',
                  'INMUEBLE_C_NOM_AMBITO', 'INMUEBLE_CV_ASEN', 'INMUEBLE_C_NOM_ASEN', 'INMUEBLE_CV_TIPO_ASEN',
                  'INMUEBLE_C_TIPO_ASEN', 'INMUEBLE_CV_CODIGO_POSTAL', 'INMUEBLE_C_DESC_UBICACION',
                  'INMUEBLE_LATITUD', 'INMUEBLE_LONGITUD', 'SOSTENIMIENTO_CV_CONTROL', 'SOSTENIMIENTO_C_CONTROL',
                  'SOSTENIMIENTO_CV_SUBCONTROL', 'SOSTENIMIENTO_C_SUBCONTROL', 'SOSTENIMIENTO_CV_DEPENDENCIAN1',
                  'SOSTENIMIENTO_C_DEPENDENCIAN1', 'SOSTENIMIENTO_CV_DEPENDENCIAN2', 'SOSTENIMIENTO_C_DEPENDENCIAN2',
                  'SOSTENIMIENTO_CV_DEPENDENCIAN3', 'SOSTENIMIENTO_C_DEPENDENCIAN3', 'SOSTENIMIENTO_CV_DEPENDENCIAN4',
                   'SOSTENIMIENTO_C_DEPENDENCIAN4', 'DEPOPERATIVA_CV_DEPENDENCIAN5', 'DEPOPERATIVA_C_DEPENDENCIAN5',
                   'CONTACTO_CV_CARGO', 'CONTACTO_C_CARGO', 'CONTACTO_CV_TIPODIRECTOR', 'CONTACTO_C_TIPODIRECTOR',
                   'CONTACTO_C_ASOCIACION', 'CONTACTO_C_CURP', 'CONTACTO_C_RFC', 'CONTACTO_C_NOMBRE', 
                   'CONTACTO_C_APELLIDO1', 'CONTACTO_C_APELLIDO2', 'CONTACTO_C_TELEFONO', 'CONTACTO_C_CELULAR',
                   'CONTACTO_C_EMAIL', 'CONTACTO_C_EXTENSION', 'CONTACTO_C_PWEB', 'SUPERVISION_CV_CCT', 'JEFSEC_CV_CCT',
                   'SERREG_CV_CCT', 'INSTITUCION_PLANTEL', 'C_TURNO_1', 'C_TURNO_2', 'C_TURNO_3',
                   'TIPONIVELSUB_CV_SERVICION1', 'TIPONIVELSUB_C_SERVICION1', 'TIPONIVELSUB_CV_SERVICION2',
                   'TIPONIVELSUB_C_SERVICION2', 'TIPONIVELSUB_CV_SERVICION3', 'TIPONIVELSUB_C_SERVICION3',
                   'C_SERVICIO_CAM', 'CARACTERISTCA_CV_CARACTERIZAN1', 'CARACTERISTCA_C_CARACTERIZAN1',
                   'CARACTERISTCA_CV_CARACTERIZAN2', 'CARACTERISTCA_C_CARACTERIZAN2')
        export_order = fields


class PersonasResource(resources.ModelResource):
    assigned_to = fields.Field(
        column_name='assigned_to',
        attribute='assigned_to',
        widget=ForeignKeyWidget(CustomUser, 'username')  # Ajustar para CustomUser
    )

    class Meta:
        model = PersonasData
        fields = (
            'id', 'idpersona', 'rfc', 'curp', 'nombres', 'apell_pat', 'apell_mat', 
            'nombre', 'sexo', 'nss', 'clabe', 'ing_gob', 'ing_sep', 'ing_rama',
            
        )
        export_order = fields

# ------------------------------------- Nomina -----------------------------------------
class NominaResource(resources.ModelResource):
    class Meta:
        model = NominasData
        fields = (
            'id', 'tipo_p', 'ud', 'municipio', 'localidad', 'ct', 'zonaesc', 'zona', 'prog', 
            'sub_prog', 'proyec', 'nss', 'rfc', 'curp', 'nombre', 'fech_ing', 'sexo', 'cve_plaza', 
            'nivel_cm', 'status_p', 'mot_pla', 'num_cheq', 'qna_pago', 'p_desde', 'p_hasta', 
            'liquido', 'comodin', 'trailers','clabe', 'fuente',
        )
        export_order = fields 

# ----------------------------- Plazas ----------------------------------------------------
class PlazaResource(resources.ModelResource):
    class Meta:
        model = PlazasData
        fields = ( 'id', 'rfc', 'curp', 'ct', 'partida', 'unidad', 'subunidad', 'categoria',
                  'horas', 'plaza', 'nivel_cm', 'pzareq', 'nivel_pto', 'docto_pla',
                  'desde_pla', 'hasta_pla', 'docto_pro', 'desde_pro', 'hasta_pro', 
                  'status_s', 'motivo_s', 'docto_s', 'desde_s', 'hasta_s', 'tipmov_s',
                  'situacion', 'trailers','cve_plaza', 'idfone', 'spd',
                  'rfc_ok', 'normalista', 'plazafone'
                  )
        export_order = fields 
        
# ----------------------------- Analitico ------------------------------------------------
class AnaliticoResource(resources.ModelResource):
    class Meta:
        model = AnaliticoData
        fields = ('id', 'llave', 'reporte_pago_2421', 'num', 'ct', 'zona_fone', 'ct_fone',
                'nivel_ct', 'cve_clasificador', 'cve_plaza', 'cve_plaza_sin_esp',
                'cve_plaza_fone', 'unid_subunid', 'nivel_educ', 'fecha_crea', 'categoria',
                'base_conf', 'usicamm', 'descripcion', 'nivel_pto', 'tipo_plaza', 'plazas',
                'horas', 'hrs', 'modelo', 'fortalecim', 'directivas', 'programa','sub_prog',
                'nivel_cm', 'zona_eco', 'zonas_iguales', 'desde_s', 'hasta_s', 'status_s', 
                'motivo_s', 'status', 'nombre_completo', 'en_lic_des', 'reanuda_en', 'resguardo',
                'docto_resg', 'docto_resg_v2', 'motivo', 'desde', 'hasta', 'rfc', 'curp', 'nombre',
                'paterno', 'materno', 'nombres', 'cve_estado_civil', 'ingreso_gob', 'ingreso_sep', 
                'ingreso_rama', 'nss', 'cve_estudio', 'cp_fernando', 'centro', 'canc', 'vac', 
                'lic10', 'lic07', 'lic11', 'trece', 'quince', 'resg'
        )
        export_order = fields 
        
        
        
 # ------------------------------- MDP ----------------------------     
class MDPResource(resources.ModelResource):
    class Meta:
        model = MDPData
        fields = ('id', 'NUM','ENTIDAD_FEDERATIVA', 'curp','rfc', 'nombre',
            'CODIGO_POSTAL','cve_plaza','ESTATUS_ACTUAL_DE_LA_PLAZA',
            'ESTATUS_DEL_NOMBRAMIENTO','MOVIMIENTO', 'CODIGO_DEL_MOVIMIENTO','ALTA_VIGENTE',
            'DESCRIPCION','FECHA_INICIAL', 'FECHA_FINAL','FECHA_DE_BAJA', 'REGIMEN',
            'NUM_DE_TICKET_MAI','FOLIO_REGISTRO_EXCEPCION','REGISTRO_EXTEMPORANEO','FECHA_DE_REGISTRO',
        )
        export_order = fields       
        
   
class Lista_NegraResource(resources.ModelResource):
    class Meta:
        model = ListaNegraData
        fields = ('id', 'sec', 'tipo', 'concepto', 'ct', 'rfc', 'curp', 'nombre', 
            'cve_plaza', 'desde', 'hasta', 'motivo', 'dup', 'usuario'
        )
        export_order = fields    
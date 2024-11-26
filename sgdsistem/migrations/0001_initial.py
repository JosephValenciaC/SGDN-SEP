# Generated by Django 5.1.3 on 2024-11-22 18:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nominas_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CV_CCT', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Baja', 'Baja'), ('Completado', 'Completado')], default='Activo', max_length=30, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('prioridad', models.CharField(blank=True, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], default='Media', max_length=10, null=True)),
                ('creado', models.CharField(blank=True, max_length=20, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('fotografia_de_la_ubicacion', models.ImageField(blank=True, null=True, upload_to='ubicacion_photos/')),
                ('C_NOMBRE', models.CharField(blank=True, max_length=100, null=True)),
                ('CV_TIPO', models.CharField(blank=True, max_length=100, null=True)),
                ('C_TIPO', models.CharField(blank=True, max_length=100, null=True)),
                ('CV_ADMINISTRATIVA', models.CharField(blank=True, max_length=100, null=True)),
                ('C_ADMINISTRATIVA', models.CharField(blank=True, max_length=100, null=True)),
                ('CV_ESTATUS', models.CharField(blank=True, max_length=10, null=True)),
                ('C_ESTATUS', models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default=' ', max_length=10, null=True)),
                ('F_FUNDACION', models.CharField(blank=True, max_length=15, null=True)),
                ('ALTA_SISTEMA', models.CharField(blank=True, max_length=15, null=True)),
                ('CAMBIO', models.CharField(blank=True, max_length=15, null=True)),
                ('CLAUSURA', models.CharField(blank=True, max_length=15, null=True)),
                ('REAPERTURA', models.CharField(blank=True, max_length=15, null=True)),
                ('REAPERTURA_CON_CAMBIO', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_INMUEBLE', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_VIALIDAD_PRINCIPAL', models.CharField(blank=True, max_length=150, null=True)),
                ('INMUEBLE_C_VIALIDAD_DERECHA', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_VIALIDAD_IZQUIERDA', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_VIALIDAD_POSTERIOR', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_N_EXTNUM', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_EXTALF', models.CharField(blank=True, max_length=50, null=True)),
                ('INMUEBLE_N_INTNUM', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_INTALF', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_ENT', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_NOM_ENT', models.CharField(blank=True, max_length=50, null=True)),
                ('INMUEBLE_CV_MUN', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_NOM_MUN', models.CharField(blank=True, max_length=15, null=True)),
                ('Zona_Economica', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_LOC', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_NOM_LOC', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_AMBITO', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_NOM_AMBITO', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_ASEN', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_NOM_ASEN', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_TIPO_ASEN', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_TIPO_ASEN', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_CV_CODIGO_POSTAL', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_C_DESC_UBICACION', models.CharField(blank=True, max_length=350, null=True)),
                ('INMUEBLE_LATITUD', models.CharField(blank=True, max_length=15, null=True)),
                ('INMUEBLE_LONGITUD', models.CharField(blank=True, max_length=15, null=True)),
                ('SOSTENIMIENTO_CV_CONTROL', models.CharField(blank=True, max_length=15, null=True)),
                ('SOSTENIMIENTO_C_CONTROL', models.CharField(blank=True, max_length=15, null=True)),
                ('SOSTENIMIENTO_CV_SUBCONTROL', models.CharField(blank=True, max_length=15, null=True)),
                ('SOSTENIMIENTO_C_SUBCONTROL', models.CharField(blank=True, max_length=15, null=True)),
                ('SOSTENIMIENTO_CV_DEPENDENCIAN1', models.CharField(blank=True, max_length=3, null=True)),
                ('SOSTENIMIENTO_C_DEPENDENCIAN1', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_CV_DEPENDENCIAN2', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_C_DEPENDENCIAN2', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_CV_DEPENDENCIAN3', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_C_DEPENDENCIAN3', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_CV_DEPENDENCIAN4', models.CharField(blank=True, max_length=150, null=True)),
                ('SOSTENIMIENTO_C_DEPENDENCIAN4', models.CharField(blank=True, max_length=150, null=True)),
                ('DEPOPERATIVA_CV_DEPENDENCIAN5', models.CharField(blank=True, max_length=150, null=True)),
                ('DEPOPERATIVA_C_DEPENDENCIAN5', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_CV_CARGO', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_C_CARGO', models.CharField(blank=True, max_length=150, null=True)),
                ('CONTACTO_CV_TIPODIRECTOR', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_C_TIPODIRECTOR', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_C_ASOCIACION', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_C_CURP', models.CharField(blank=True, max_length=50, null=True)),
                ('CONTACTO_C_RFC', models.CharField(blank=True, max_length=15, null=True)),
                ('CONTACTO_C_NOMBRE', models.CharField(blank=True, max_length=150, null=True)),
                ('CONTACTO_C_APELLIDO1', models.CharField(blank=True, max_length=50, null=True)),
                ('CONTACTO_C_APELLIDO2', models.CharField(blank=True, max_length=50, null=True)),
                ('CONTACTO_C_TELEFONO', models.CharField(blank=True, max_length=10, null=True)),
                ('CONTACTO_C_CELULAR', models.CharField(blank=True, max_length=10, null=True)),
                ('CONTACTO_C_EMAIL', models.CharField(blank=True, max_length=50, null=True)),
                ('CONTACTO_C_EXTENSION', models.CharField(blank=True, max_length=10, null=True)),
                ('CONTACTO_C_PWEB', models.CharField(blank=True, max_length=150, null=True)),
                ('SUPERVISION_CV_CCT', models.CharField(blank=True, max_length=150, null=True)),
                ('JEFSEC_CV_CCT', models.CharField(blank=True, max_length=50, null=True)),
                ('SERREG_CV_CCT', models.CharField(blank=True, max_length=15, null=True)),
                ('INSTITUCION_PLANTEL', models.CharField(blank=True, max_length=15, null=True)),
                ('C_TURNO_1', models.CharField(blank=True, max_length=15, null=True)),
                ('C_TURNO_2', models.CharField(blank=True, max_length=15, null=True)),
                ('C_TURNO_3', models.CharField(blank=True, max_length=15, null=True)),
                ('TIPONIVELSUB_CV_SERVICION1', models.CharField(blank=True, max_length=15, null=True)),
                ('TIPONIVELSUB_C_SERVICION1', models.CharField(blank=True, max_length=15, null=True)),
                ('TIPONIVELSUB_CV_SERVICION2', models.CharField(blank=True, max_length=15, null=True)),
                ('TIPONIVELSUB_C_SERVICION2', models.CharField(blank=True, max_length=50, null=True)),
                ('TIPONIVELSUB_CV_SERVICION3', models.CharField(blank=True, max_length=15, null=True)),
                ('TIPONIVELSUB_C_SERVICION3', models.CharField(blank=True, max_length=15, null=True)),
                ('C_SERVICIO_CAM', models.CharField(blank=True, max_length=15, null=True)),
                ('CARACTERISTCA_CV_CARACTERIZAN1', models.CharField(blank=True, max_length=60, null=True)),
                ('CARACTERISTCA_C_CARACTERIZAN1', models.CharField(blank=True, max_length=25, null=True)),
                ('CARACTERISTCA_CV_CARACTERIZAN2', models.CharField(blank=True, max_length=15, null=True)),
                ('CARACTERISTCA_C_CARACTERIZAN2', models.CharField(blank=True, max_length=15, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_inmueble', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
                'permissions': [('add_tasks_inmueble', 'Can add inmueble in tasks app'), ('change_tasks_inmueble', 'Can change inmueble in tasks app'), ('delete_tasks_inmueble', 'Can delete inmueble in tasks app'), ('view_tasks_inmueble', 'Can view inmueble in tasks app')],
            },
        ),
    ]
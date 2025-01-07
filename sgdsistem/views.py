from django.shortcuts import render
import os
from unittest import loader
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sgdsep import settings
from sgdsistem.forms import InmueblesForm
from sgdsistem.models import Inmuebles_data, NominasData, PersonasData
from django.contrib.auth.decorators import login_required, permission_required

from sgdsistem import models


def permission_denied(request):
    return render(request, '403.html')


def error_404(request, exception):
    template_404 = '404.html'
    return render(request, template_404, status=404)



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    

from django.contrib.auth.decorators import login_required


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
            })
        else:
            login(request, user)
            return redirect('principal')


@login_required
def signout(request):
    logout(request)
    return redirect('/')
    

@login_required
def principal(request):
    return render(request, 'home.html', {
    } )



from django.db.models import Q

@login_required
def Inmuebles_home(request):
    # Obtener los parámetros de búsqueda
    search_query = request.GET.get('q', '')
    cv_inmueble = request.GET.get('cv_inmueble', '')
    estado = request.GET.get('estado', '')
    orden = request.GET.get('ordenar', '')

    # Filtro base
    inmuebles_list = Inmuebles_data.objects.filter(datecompleted__isnull=True)

    # Aplicar filtros dinámicos
    if search_query:
        inmuebles_list = inmuebles_list.filter(CV_CCT__icontains=search_query)
    if cv_inmueble:
        inmuebles_list = inmuebles_list.filter(INMUEBLE_CV_INMUEBLE__icontains=cv_inmueble)
    if estado:
        inmuebles_list = inmuebles_list.filter(estado=estado)

    # Aplicar filtros de orden
    if orden == 'az':
        inmuebles_list = inmuebles_list.order_by('CV_CCT')
    elif orden == 'za':
        inmuebles_list = inmuebles_list.order_by('-CV_CCT')
    elif orden == 'nuevo':
        inmuebles_list = inmuebles_list.order_by('-updated')  # Ordenar por fecha de actualización
    elif orden == 'viejo':
        inmuebles_list = inmuebles_list.order_by('creado')  # Ordenar por fecha de creación

    # Paginación
    paginator = Paginator(inmuebles_list, 10)  # Mostrar 20 inmuebles por página
    page = request.GET.get('page')
    inmuebles = paginator.get_page(page)

    return render(request, 'Adm_Inmuebles/inmuebles_home.html', {
        'inmuebles': inmuebles,
        'search_query': search_query,
        'orden': orden,
    })



from tablib import Dataset 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from tablib import Dataset
from sgdsistem.resource import AnaliticoResource, InmueblesResource, Lista_NegraResource, MDPResource, NominaResource, PersonasResource, PlazaResource

@login_required
def importar(request):
    if request.method == 'POST':
        inmueble_resource = InmueblesResource()
        dataset = Dataset()
        
        archivo = request.FILES['archivo']

        if archivo.name.endswith('.csv'):
            imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
        elif archivo.name.endswith(('xls', 'xlsx')):
            imported_data = dataset.load(archivo.read(), format='xlsx')
        else:
            messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
            return render(request, 'Adm_Inmuebles/importarArchivos_Inmuebles.html')

        result = inmueble_resource.import_data(dataset, dry_run=True)
        
        if not result.has_errors():
            # Realiza la importación real
            result = inmueble_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos se importaron con éxito.')
        else:
            messages.error(request, 'Se encontraron errores en la importación.')

    return render(request, 'Adm_Inmuebles/importarArchivos_Inmuebles.html')



def Detalle_inmueble(request, task_id):
    task = get_object_or_404(Inmuebles_data, pk=task_id)
    
    if request.method == 'POST':
        inmueble = InmueblesForm(request.POST, request.FILES, instance=task)

        if inmueble.is_valid():
            inmueble.save()  # Guardar los cambios en la tarea
            return redirect('Inmuebles_home')  # Redireccionar a 'Inmuebles' después de guardar
    else:
        inmueble = InmueblesForm(instance=task)
        
    return render(request, 'Adm_Inmuebles/detalle_inmueble.html', {
        'task': task,
        'inmueble': inmueble,
        'titulo': task.CV_CCT,
    })



@login_required
def importar_personas(request):
    if request.method == 'POST':
        try:
            persona_resource = PersonasResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_Personas/importarArchivos_Personas.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_Personas/importarArchivos_Personas.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_Personas/importarArchivos_Personas.html')

            # Realiza la validación inicial en modo "dry run"
            result = persona_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_Personas/importarArchivos_Personas.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            persona_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos de Personas se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_Personas/importarArchivos_Personas.html')

    return render(request, 'Adm_Personas/importarArchivos_Personas.html')


@login_required
def personas_home(request):
    # Obtener los parámetros de búsqueda
    nombre = request.GET.get('nombre', '')
    rfc = request.GET.get('rfc', '')
    curp = request.GET.get('curp', '')

    # Filtro base
    personas_list = PersonasData.objects.all()

    # Aplicar filtros dinámicos
    if nombre:
        personas_list = personas_list.filter(nombre__icontains=nombre)
    if rfc:
        personas_list = personas_list.filter(rfc__icontains=rfc)
    if curp:
        personas_list = personas_list.filter(curp__icontains=curp)
        
         # Paginación
    paginator = Paginator(personas_list, 10)
    page_number = request.GET.get('page')
    personas = paginator.get_page(page_number)


    return render(request, 'Adm_Personas/personas_home.html', {
        'personas': personas,
        'nombre': nombre,
        'rfc': rfc,
        'curp': curp,
    })

from django.shortcuts import render, get_object_or_404, redirect

def Detalle_persona(request, persona_id):
    persona = get_object_or_404(PersonasData, pk=persona_id)

    if request.method == 'POST':
        persona_form = PersonasDataForm(request.POST, request.FILES, instance=persona)

        if persona_form.is_valid():
            persona_form.save()  # Guardar los cambios en la persona
            return redirect('personas_home')  # Redireccionar al listado de personas después de guardar
    else:
        persona_form = PersonasDataForm(instance=persona)

    return render(request, 'Adm_Personas/detalle_persona.html', {
        'persona': persona,
        'persona_form': persona_form,
        'titulo': persona.nombre,  # Aquí puedes usar el nombre o algún campo representativo de la persona
    })






import os
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from io import BytesIO

def convertir_csv_a_excel(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        archivo_csv = request.FILES['csv_file']

        # Obtener el nombre original del archivo sin la extensión
        nombre_original = os.path.splitext(archivo_csv.name)[0]

        # Ruta temporal donde se guardará el archivo CSV cargado
        carpeta_destino = 'temp/'
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)  # Crear el directorio si no existe

        # Guardar el archivo CSV cargado
        csv_file_path = os.path.join(carpeta_destino, 'uploaded.csv')
        fs = FileSystemStorage(location=carpeta_destino)
        fs.save('uploaded.csv', archivo_csv)

        # Intentar leer el archivo CSV con codificaciones diferentes
        try:
            # Intenta leer con utf-8
            df = pd.read_csv(csv_file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                # Si falla, intenta con latin1
                df = pd.read_csv(csv_file_path, encoding='latin1')
            except UnicodeDecodeError:
                try:
                    # Si aún falla, intenta con ISO-8859-1
                    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
                except Exception as e:
                    return HttpResponse(f'Error al leer el archivo CSV: {str(e)}', status=400)

        # Crear el archivo Excel en memoria
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        # Configurar el nombre del archivo de salida
        nombre_excel = f"{nombre_original}.xlsx"

        # Responder con el archivo Excel para descarga
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{nombre_excel}"'
        return response

    # Renderizar la página de carga si no es POST
    return render(request, 'functions/convertir_csv.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import AnaliticoDataForm, EditUserForm, Lista_NegraForm, MDPForm, NominasDataForm, PersonasDataForm, PlazasDataForm, UserForm


# Usar el modelo de usuario personalizado
CustomUser = get_user_model()

def usuarios(request):
    users = CustomUser.objects.all()  # Usar CustomUser en lugar de User
    return render(request, 'gestion_usuarios/user_list.html', {'users': users})


CustomUser = get_user_model()

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario utilizando el modelo personalizado
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('usuarios')  # Redirige a la lista de usuarios
    else:
        form = UserForm()

    return render(request, 'gestion_usuarios/create_user.html', {'form': form})



@login_required
@permission_required('sgdsistem.administrar_Inmueble', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado exitosamente.")
            return redirect('usuarios')  # Redirige a la lista de usuarios
    else:
        form = EditUserForm(instance=user)

    return render(request, 'gestion_usuarios/edit_user.html', {'form': form, 'user': user})




# -------------------Configuracion--------------------
# views.py

from django.shortcuts import render

def configuracion_view(request):
    return render(request, 'config/configuracion.html')



# -------------------Nominas--------------------

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AnaliticoData, ListaNegraData, MDPData, NominasData, PlazasData

from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import render

from django.db.models import Sum

@login_required
def nominas_home(request):
    # Parámetros de búsqueda
    search_query = request.GET.get('q', '')
    nombre = request.GET.get('nombre', '')
    curp = request.GET.get('curp', '')
    quincena = request.GET.get('quincena', '')
    ct = request.GET.get('ct', '')
    cve_plaza = request.GET.get('cve_plaza', '')

    # Filtrado de registros
    nominas_list = NominasData.objects.all()
    if search_query:
        nominas_list = nominas_list.filter(rfc__icontains=search_query)
    if nombre:
        nominas_list = nominas_list.filter(nombre__icontains=nombre)
    if curp:
        nominas_list = nominas_list.filter(curp__icontains=curp)
    if quincena:
        nominas_list = nominas_list.filter(qna_pago__icontains=quincena)
    if ct:
        nominas_list = nominas_list.filter(ct__icontains=ct)
    if cve_plaza:
        nominas_list = nominas_list.filter(cve_plaza__icontains=cve_plaza)
        
    nominas_list = nominas_list.order_by('cve_plaza')  # Orden ascendente (A-Z)

    # Calcular la suma del campo liquido
    total_liquido = nominas_list.aggregate(Sum('liquido'))['liquido__sum'] or 0

    # Paginación
    paginator = Paginator(nominas_list, 10)
    page_number = request.GET.get('page')
    nominas = paginator.get_page(page_number)

    return render(request, 'Adm_Nominas/nominas_home.html', {
        'nominas': nominas,
        'search_query': search_query,
        'nombre': nombre,
        'curp': curp,
        'quincena': quincena,
        'ct': ct,
        'cve_plaza': cve_plaza,
        'total_liquido': total_liquido,  # Pasa el total de liquido al contexto
    })


@login_required
def detalle_nomina(request, nomina_id):
    nomina = get_object_or_404(NominasData, pk=nomina_id)

    if request.method == 'POST':
        nomina_form = NominasDataForm(request.POST, request.FILES, instance=nomina)

        if nomina_form.is_valid():
            nomina_form.save()
            return redirect('nominas_home') 
    else:
        nomina_form = NominasDataForm(instance=nomina)

    return render(request, 'Adm_Nominas/detalle_nomina.html', {
        'nomina': nomina,
        'nomina_form': nomina_form,
    })


from tablib import Dataset
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse

@login_required
def importar_nominas(request):
    if request.method == 'POST':
        try:
            nomina_resource = NominaResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_Nominas/importarArchivos_nomina.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_Nominas/importarArchivos_nomina.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_Nominas/importarArchivos_nomina.html')

            # Realiza la validación inicial en modo "dry run"
            result = nomina_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_Nominas/importarArchivos_nomina.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            nomina_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_Nominas/importarArchivos_nomina.html')

    return render(request, 'Adm_Nominas/importarArchivos_nomina.html')


# ----------------------------- Plazas --------------------------------------

@login_required
def plazas_home(request):
    # Parámetros de búsqueda
    search_query = request.GET.get('q', '')
    ct = request.GET.get('ct', '')
    cve_plaza = request.GET.get('cve_plaza', '')

    # Filtrado de registros
    plazas_list = PlazasData.objects.all()
    if search_query:
        plazas_list = plazas_list.filter(rfc__icontains=search_query)
    if ct:
        plazas_list = plazas_list.filter(ct__icontains=ct)
    if cve_plaza:
        plazas_list = plazas_list.filter(cve_plaza__icontains=cve_plaza)
        
    plazas_list = plazas_list.order_by('cve_plaza')  # Orden ascendente (A-Z)

    # Paginación
    paginator = Paginator(plazas_list, 10)
    page_number = request.GET.get('page')
    plazas = paginator.get_page(page_number)

    return render(request, 'Adm_plazas/plazas_home.html', {
        'plazas': plazas,
        'search_query': search_query,
        'ct': ct,
        'cve_plaza': cve_plaza,
    })

@login_required
def detalle_plaza(request, plaza_id):
    plaza = get_object_or_404(PlazasData, pk=plaza_id)

    if request.method == 'POST':
        plaza_form = PlazasDataForm(request.POST, request.FILES, instance=plaza)

        if plaza_form.is_valid():
            plaza_form.save()
            return redirect('plazas_home') 
    else:
        plaza_form = PlazasDataForm(instance=plaza)

    return render(request, 'Adm_Plazas/detalle_plazas.html', {
        'plaza': plaza,
        'plaza_form': plaza_form,
    })
    
    
@login_required
def importar_plazas(request):
    if request.method == 'POST':
        try:
            plaza_resource = PlazaResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_Plazas/importar_Plazas.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_Plazas/importar_Plazas.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_Plazas/importar_Plazas.html')

            # Realiza la validación inicial en modo "dry run"
            result = plaza_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_Plazas/importar_Plazas.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            plaza_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos de Plazas se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_Plazas/importar_Plazas.html')

    return render(request, 'Adm_Plazas/importar_Plazas.html')


# ----------------------- Analitio -----------------------------------------

@login_required
def analitico_home(request):
    # Parámetros de búsqueda
    search_query = request.GET.get('q', '')
    rfc = request.GET.get('rfc', '')
    ct = request.GET.get('ct', '')
    desde = request.GET.get('desde', '')
    hasta = request.GET.get('hasta', '')
    motivo = request.GET.get('motivo', '')
    curp = request.GET.get('curp', '')
    cve_plaza_edo = request.GET.get('cve_plaza_edo', '')

    # Filtrado de registros
    analitico_list = AnaliticoData.objects.all()

    if rfc:
        analitico_list = analitico_list.filter(rfc__icontains=rfc)
    if ct:
        analitico_list = analitico_list.filter(ct__icontains=ct)
    if motivo:
        analitico_list = analitico_list.filter(motivo__icontains=motivo)
    if curp:
        analitico_list = analitico_list.filter(curp__icontains=curp)
    if cve_plaza_edo:
        analitico_list = analitico_list.filter(cve_plaza_edo__icontains=cve_plaza_edo)
    if desde:
        analitico_list = analitico_list.filter(desde__icontains=desde)
    if hasta:
        analitico_list = analitico_list.filter(hasta__icontains=hasta)
    

    # Paginación
    paginator = Paginator(analitico_list, 10)
    page_number = request.GET.get('page')
    analiticos = paginator.get_page(page_number)

    return render(request, 'Adm_Analitico/analitico_home.html', {
        'analiticos': analiticos,
        'rfc': rfc,
        'ct': ct,
        'desde': desde,
        'hasta': hasta,
        'motivo': motivo,
        'curp': curp,
        'cve_plaza_edo': cve_plaza_edo,
    })


@login_required
def detalle_analitico(request, analitico_id):
    analiticos = get_object_or_404(AnaliticoData, pk=analitico_id)

    if request.method == 'POST':
        analitico_form = AnaliticoDataForm(request.POST, request.FILES, instance=analiticos)

        if analitico_form.is_valid():
            analitico_form.save()
            return redirect('analiticos_home') 
    else:
        analitico_form = AnaliticoDataForm(instance=analiticos)

    return render(request, 'Adm_analitico/detalle_analitico.html', {
        'analiticos': analiticos,
        'analitico_form': analitico_form,
    })
    
    
@login_required
def importar_analitico(request):
    if request.method == 'POST':
        try:
            analitico_resource = AnaliticoResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_Analitico/importar_analitico.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_Analitico/importar_analitico.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_Analitico/importar_analitico.html')

            # Realiza la validación inicial en modo "dry run"
            result = analitico_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_Analitico/importar_analitico.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            analitico_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos de Analitico se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_Analitico/importar_analitico.html')

    return render(request, 'Adm_Analitico/importar_analitico.html')


# -------------------------------------- MDP -----------------------------------

@login_required
def mdp_home(request):
    # Parámetros de búsqueda
    search_query = request.GET.get('q', '')
    rfc = request.GET.get('rfc', '')
    ct = request.GET.get('ct', '')
    desde = request.GET.get('desde', '')
    hasta = request.GET.get('hasta', '')
    motivo = request.GET.get('motivo', '')
    curp = request.GET.get('curp', '')
    cve_plaza_edo = request.GET.get('cve_plaza_edo', '')

    # Filtrado de registros
    mdp_list = MDPData.objects.all()

    if rfc:
        mdp_list = mdp_list.filter(rfc__icontains=rfc)
    if ct:
        mdp_list = mdp_list.filter(ct__icontains=ct)
    if desde and hasta:
        mdp_list = mdp_list.filter(campo_numerico__icontains=hasta)
    if motivo:
        mdp_list = mdp_list.filter(motivo__icontains=motivo)
    if curp:
        mdp_list = mdp_list.filter(curp__icontains=curp)
    if cve_plaza_edo:
        mdp_list = mdp_list.filter(cve_plaza_edo__icontains=cve_plaza_edo)

    # Paginación
    paginator = Paginator(mdp_list, 10)
    page_number = request.GET.get('page')
    mdps = paginator.get_page(page_number)

    return render(request, 'Adm_MDP/mdp_home.html', {
        'mdps': mdps,
        'rfc': rfc,
        'ct': ct,
        'desde': desde,
        'hasta': hasta,
        'motivo': motivo,
        'curp': curp,
        'cve_plaza_edo': cve_plaza_edo,
    })

@login_required
def detalle_mdp(request, mdp_id):
    mdps = get_object_or_404(MDPData, pk=mdp_id)

    if request.method == 'POST':
        mdp_form = MDPForm(request.POST, request.FILES, instance=mdps)

        if mdp_form.is_valid():
            mdp_form.save()
            return redirect('mdp_home') 
    else:
        mdp_form = MDPForm(instance=mdps)

    return render(request, 'Adm_MDP/detalle_mdp.html', {
        'mdps': mdps,
        'mdp_form': mdp_form,
    })
    
    
@login_required
def importar_mdp(request):
    if request.method == 'POST':
        try:
            mdp_resource = MDPResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_MDP/importar_mdp.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_MDP/importar_mdp.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_MDP/importar_mdp.html')

            # Realiza la validación inicial en modo "dry run"
            result = mdp_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_MDP/importar_mdp.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            mdp_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos de mdp se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_MDP/importar_mdp.html')

    return render(request, 'Adm_MDP/importar_mdp.html')



# -------------------------------------- Lista Negra -----------------------------------

@login_required
def lista_negra_home(request):
    # Parámetros de búsqueda
    rfc = request.GET.get('rfc', '').strip()
    curp = request.GET.get('curp', '').strip()
    nombre = request.GET.get('nombre', '').strip()
    cve_plaza = request.GET.get('cve_plaza', '').strip()
    desde = request.GET.get('desde', '').strip()
    hasta = request.GET.get('hasta', '').strip()

    # Filtrado de registros
    lista_negra_list = ListaNegraData.objects.all()

    if rfc:
        lista_negra_list = lista_negra_list.filter(rfc__icontains=rfc)
    if curp:
        lista_negra_list = lista_negra_list.filter(curp__icontains=curp)
    if nombre:
        lista_negra_list = lista_negra_list.filter(nombre__icontains=nombre)
    if cve_plaza:
        lista_negra_list = lista_negra_list.filter(cve_plaza__icontains=cve_plaza)
    if desde:
        lista_negra_list = lista_negra_list.filter(desde__icontains=desde)
    if hasta:
        lista_negra_list = lista_negra_list.filter(hasta__icontains=hasta)

    # Paginación
    paginator = Paginator(lista_negra_list, 20)
    page_number = request.GET.get('page')
    lista_negra = paginator.get_page(page_number)

    # Renderizar plantilla
    return render(request, 'Adm_Lista_Negra/lista_negra_home.html', {
        'lista_negra': lista_negra,
        'rfc': rfc,
        'curp': curp,
        'nombre': nombre,
        'cve_plaza': cve_plaza,
        'desde': desde,
        'hasta': hasta,
    })


@login_required
def detalle_lista_negra(request, lista_negra_id):
    # Obtener objeto o lanzar 404 si no existe
    lista_negra = get_object_or_404(ListaNegraData, pk=lista_negra_id)

    if request.method == 'POST':
        # Procesar formulario
        lista_negra_form = Lista_NegraForm(request.POST, request.FILES, instance=lista_negra)
        if lista_negra_form.is_valid():
            lista_negra_form.save()
            return redirect('lista_negra_home')  # Redirigir a la lista principal
    else:
        # Inicializar formulario con datos del objeto
        lista_negra_form = Lista_NegraForm(instance=lista_negra)

    # Renderizar plantilla
    return render(request, 'Adm_Lista_Negra/detalle_lista_negra.html', {
        'lista_negra': lista_negra,
        'lista_negra_form': lista_negra_form,
    })

    
    
@login_required
def importar_lista_negra(request):
    if request.method == 'POST':
        try:
            lista_negra_resource = Lista_NegraResource()
            dataset = Dataset()

            archivo = request.FILES.get('archivo')
            if not archivo:
                messages.error(request, 'No se proporcionó ningún archivo para la importación.')
                return render(request, 'Adm_Lista_Negra/importar_lista_negra.html')

            # Determina el formato del archivo y lo carga en el dataset
            if archivo.name.endswith('.csv'):
                imported_data = dataset.load(archivo.read().decode('utf-8'), format='csv')
            elif archivo.name.endswith(('xls', 'xlsx')):
                imported_data = dataset.load(archivo.read(), format='xlsx')
            else:
                messages.error(request, 'El archivo no es ni un archivo CSV ni un archivo Excel válido.')
                return render(request, 'Adm_Lista_Negra/importar_lista_negra.html')

            # Verifica si los datos fueron cargados correctamente
            if not imported_data:
                messages.error(request, 'No se pudieron cargar los datos del archivo. Verifique el formato del archivo.')
                return render(request, 'Adm_Lista_Negra/importar_lista_negra.html')

            # Realiza la validación inicial en modo "dry run"
            result = lista_negra_resource.import_data(dataset, dry_run=True)

            # Muestra un resumen de los datos y los errores, si los hay
            if result.has_errors():
                error_list = []
                for row_error in result.row_errors():
                    row_number = row_error[0]
                    errors = row_error[1]
                    for error in errors:
                        error_list.append(f"Fila {row_number}: {error.error}")

                # Devuelve la lista de errores para mostrar en la vista
                messages.error(request, f"Errores encontrados: {', '.join(error_list)}")
                return render(
                    request,
                    'Adm_Lista_Negra/importar_lista_negra.html',
                    {'dataset_preview': dataset.html, 'errors': error_list}
                )

            # Si no hay errores, realiza la importación real
            lista_negra_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos de mdp se importaron con éxito.')
        except Exception as e:
            messages.error(request, f"Ocurrió un error inesperado: {str(e)}")
            return render(request, 'Adm_Lista_Negra/importar_lista_negra.html')

    return render(request, 'Adm_Lista_Negra/importar_lista_negra.html')

# ------------------------------ Consulta Global ------------------------

from django.db.models import F, Q, Value, CharField
from django.shortcuts import render
from .models import PersonasData, PlazasData, MDPData, NominasData, AnaliticoData
from django.db import connection

@login_required
def consulta_global_home(request):
    # Obtener parámetros del formulario
    rfc = request.GET.get('rfc', '').strip()
    curp = request.GET.get('curp', '').strip()
    nombre = request.GET.get('nombre', '').strip()
    cve_plaza = request.GET.get('cve_plaza', '').strip()
    desde_s = request.GET.get('desde_s', '').strip()
    hasta_s = request.GET.get('hasta_s', '9999').strip()
    status = request.GET.get('status', '').strip()  # Nuevo campo para filtrar por status
    ct = request.GET.get('ct', '')
    page = request.GET.get('page', 1)  # Número de página actual

    # Definir condiciones para "status vivo" y "bajas"
    if status == 'vivo':
        status_condition = "a.status_s IN ('01', '06') AND a.motivo_s NOT IN ('31', '32', '33', '37', '38')"
    elif status == 'bajas':
        status_condition = "a.status_s NOT IN ('01', '06') OR a.motivo_s IN ('31', '32', '33', '37', '38')"
    else:
        status_condition = "1=1"  # Sin filtro (se incluyen todos)

    # Construir la consulta SQL segura con parámetros
    query = f"""
        SELECT DISTINCT
            p.rfc,  
            p.curp, 
            p.nombre AS nombre_persona,
            pl.ct AS centro_trabajo, 
            pl.cve_plaza, 
            a.motivo_s AS motivo_plaza,
            a.desde_s AS desde,
            a.hasta_s AS hasta,
            a.status_s AS status,
            ln.motivo AS motivoln
        FROM
            sgdsistem_personasdata p
        LEFT JOIN sgdsistem_plazasdata pl 
            ON p.rfc = pl.rfc
        LEFT JOIN sgdsistem_analiticodata a 
            ON p.rfc = a.rfc
            AND p.curp = a.curp
            AND pl.cve_plaza = a.cve_plaza
        LEFT JOIN sgdsistem_listanegradata ln 
            ON p.rfc = ln.rfc
            AND p.curp = ln.curp
            AND pl.cve_plaza = ln.cve_plaza
            AND pl.ct = ln.ct
            WHERE
                (p.rfc LIKE %s OR %s = '') AND
                (p.curp LIKE %s OR %s = '') AND
                (p.nombre LIKE %s OR %s = '') AND
                (pl.cve_plaza LIKE %s OR %s = '') AND
                (a.desde_s >= %s OR %s = '') AND
                (a.desde_s < 7000) AND  -- Excluir valores de 7000 en adelante
                (a.hasta_s <= %s OR %s = '') AND
                {status_condition}
            ORDER BY pl.cve_plaza;
    """

    # Parámetros para evitar inyección SQL
    parametros = [f"%{rfc}%", rfc, f"%{curp}%", curp, f"%{nombre}%", nombre, f"%{cve_plaza}%", cve_plaza, desde_s, desde_s, hasta_s, hasta_s]

    # Ejecutar la consulta y obtener resultados
    with connection.cursor() as cursor:
        cursor.execute(query, parametros)
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        
    # Paginación: dividir los resultados en páginas de 20 elementos
    paginator = Paginator(resultados, 20)
    resultados = paginator.get_page(page)

    # Renderizar resultados en la plantilla
    return render(request, 'Adm_ConsultaGlobal/consulta_global.html', {
        'resultados': resultados,
        'rfc': rfc,
        'curp': curp,
        'nombre': nombre,
        'cve_plaza': cve_plaza,
        'ct': ct,
        'desde_s': desde_s,
        'hasta_s': hasta_s,
        'request': request,
        'status': status,
    })



from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os
from PIL import Image

def generar_pdf_nominas(request):
    rfc = request.GET.get('rfc')
    if not rfc:
        return HttpResponse("No se proporcionó un RFC válido.", status=400)

    # Obtener los datos de la nómina con el RFC proporcionado
    nominas = NominasData.objects.filter(rfc=rfc)
    if not nominas:
        return HttpResponse("No se encontraron nóminas para el RFC proporcionado.", status=404)

    # Calcular el total líquido
    total_liquido = sum(float(nomina.liquido) for nomina in nominas)

    # Crear la respuesta HTTP para el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="reporte_nomina_{rfc}.pdf"'

    # Crear el objeto canvas
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Rutas de imágenes
    logo_path = os.path.join(os.path.dirname(__file__), 'static', 'images', 'gob_mich_full.png')
    logo_path2 = os.path.join(os.path.dirname(__file__), 'static', 'images', 'OIP.jpg')
    fondo = os.path.join(os.path.dirname(__file__), 'static', 'images', 'fondo.jpg')

    # Hacer la imagen más transparente usando Pillow
    try:
        original_image = Image.open(fondo).convert("RGBA")
        # Crear un nuevo canal alfa para la transparencia
        alpha = original_image.split()[3]
        alpha = alpha.point(lambda p: p * 0.1)  # Reducir la opacidad al 50%
        original_image.putalpha(alpha)

        # Guardar la imagen temporalmente con transparencia ajustada
        temp_path = os.path.join(os.path.dirname(__file__), 'static', 'images', 'fondo_transparente.png')
        original_image.save(temp_path, format="PNG")
        
        # Dibujar la imagen de fondo en el PDF
        pdf.drawImage(temp_path, -10, - 20, width=650, height=650, mask='auto')
    except Exception as e:
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, 50, f"Error al procesar la imagen de fondo: {e}")

    # Dibujar logos
    try:
        pdf.drawImage(logo_path, 50, height - 170, width=180, height=190, preserveAspectRatio=True, mask='auto')
    except FileNotFoundError:
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, height - 70, "Error: Logo no encontrado.")

    try:
        pdf.drawImage(logo_path2, width - 150, height - 160, width=100, height=170, preserveAspectRatio=True, mask='auto')
    except FileNotFoundError:
        pdf.setFont("Helvetica", 10)
        pdf.drawString(width - 150, height - 70, "Error: Logo no encontrado.")

    # Encabezado
    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(colors.HexColor("#004d99"))
    pdf.drawCentredString(width / 2, height - 180, "Reporte de Nóminas")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(colors.black)
    pdf.drawString(50, height - 200, f"RFC: {rfc}")
    pdf.drawString(50, height - 220, f"Nombre: {nominas[0].nombre if nominas else 'N/A'}")
    pdf.drawString(50, height - 240, f"CURP: {nominas[0].curp if nominas else 'N/A'}")

    # Línea horizontal
    pdf.setStrokeColor(colors.HexColor("#004d99"))
    pdf.line(50, height - 250, width - 50, height - 250)

    # Tabla de datos
    data = [["Centro de Trabajo", "Clave Plaza", "Quincena Pago", "Líquido"]]
    for nomina in nominas:
        data.append([nomina.ct, nomina.cve_plaza, nomina.qna_pago, f"${float(nomina.liquido):,.2f}"])

    # Total
    data.append(["", "", "Total Líquido:", f"${total_liquido:,.2f}"])

    # Crear la tabla
    table = Table(data, colWidths=[150, 150, 100, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#004d99")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f9f9f9")),
        ('GRID', (0, 0), (-1, -1), 1, colors.gray),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TEXTCOLOR', (-2, -1), (-1, -1), colors.HexColor("#004d99")),
        ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (-2, -1), (-1, -1), 'RIGHT')
    ]))

    # Dibujar tabla
    table.wrapOn(pdf, width, height)
    table.drawOn(pdf, 50, height - 400)

    # Pie de página
    pdf.setFont("Helvetica", 10)
    pdf.setFillColor(colors.gray)
    pdf.drawString(50, 50, "Este reporte fue generado por el SGDN-SEP.")

    # Finalizar el PDF
    pdf.save()

    return response


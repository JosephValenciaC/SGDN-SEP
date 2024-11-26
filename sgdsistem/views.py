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
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sgdsep import settings
from sgdsistem.forms import InmueblesForm
from sgdsistem.models import Inmuebles_data


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
    paginator = Paginator(inmuebles_list, 20)
    page = request.GET.get('page')
    inmuebles = paginator.get_page(page)

    return render(request, 'Adm_Inmuebles/inmuebles_home.html', {
        'inmuebles': inmuebles,
        'search_query': search_query,
        'orden': orden,
    })


from tablib import Dataset 
from django.http import HttpResponse
from django.shortcuts import render
from tablib import Dataset
from sgdsistem.resource import InmueblesResource

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
            return render(request, 'Adm_Inmuebles/importarArchivos_nomina.html')

        result = inmueble_resource.import_data(dataset, dry_run=True)
        
        if not result.has_errors():
            # Realiza la importación real
            result = inmueble_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos se importaron con éxito.')
        else:
            messages.error(request, 'Se encontraron errores en la importación.')

    return render(request, 'Adm_Inmuebles/importarArchivos_nomina.html')



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


import os
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd

import os
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from io import BytesIO
from django.http import JsonResponse
import os

def convertir_csv_a_excel(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        archivo_csv = request.FILES['csv_file']

        # Ruta donde se guardará el archivo CSV cargado
        carpeta_destino = 'temp/'
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)  # Crea el directorio si no existe

        # Guardar el archivo CSV cargado
        csv_file_path = os.path.join(carpeta_destino, archivo_csv.name)
        with open(csv_file_path, 'wb+') as destination:
            for chunk in archivo_csv.chunks():
                destination.write(chunk)

        # Intentar leer el archivo CSV con codificaciones diferentes
        try:
            df = pd.read_csv(csv_file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(csv_file_path, encoding='latin1')
            except UnicodeDecodeError:
                df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

        # Convertir CSV a Excel
        excel_file_name = os.path.splitext(archivo_csv.name)[0] + '.xlsx'
        excel_file_path = os.path.join(carpeta_destino, excel_file_name)
        df.to_excel(excel_file_path, index=False)

        # Enviar la URL del archivo al template
        excel_url = f'/media/{excel_file_name}'
        return render(request, 'functions/convertir_csv.html', {
            'mensaje': "Archivo convertido exitosamente.",
            'excel_url': excel_url
        })

    return render(request, 'functions/convertir_csv.html')






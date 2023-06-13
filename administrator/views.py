import json
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from administrator.forms import ChangePassForm, CreateAdminForm, EditAdminForm
from student.models import Student
from .models import Administrator
from django.db.models import Count

def get_administrator(id):
    try:
        return Administrator.objects.get(id=id)
    except Administrator.DoesNotExist:
        return None

@login_required
def dashboard(request):
    bar = (
        Student.objects
        .values('university__name')
        .annotate(total_discapacitados=Count('disability'))
    )

    pie = (
        Student.objects
        .values('sex__gender')
        .annotate(count=Count('sex__gender'))
    )

    # Calcula el total de estudiantes
    total_estudiantes = sum(d['count'] for d in pie)

    # Calcula el porcentaje de cada sexo
    for d in pie:
        d['porcentaje'] = round((d['count'] / total_estudiantes) * 100, 2)

    pie2 = (
        Student.objects
        .values('disability__type')
        .annotate(count=Count('disability__type'))
    )

    # Calcula el total de estudiantes
    total_estudiantes = sum(d['count'] for d in pie2)

    # Calcula el porcentaje de cada discapacidad
    for d in pie2:
        d['porcentaje'] = round((d['count'] / total_estudiantes) * 100, 2)

    bar_json = json.dumps(list(bar))
    pie_json = json.dumps(list(pie))
    pie2_json = json.dumps(list(pie2))

    return render(request, 'dashboard.html', {
        'title': 'Dashboard',
        'panel': 'Dashboard',
        'bar': bar_json,
        'pie': pie_json,
        'pie2': pie2_json
    })

def signout(request):
    # Cierra la sesión del usuario y redirige a la página de inicio
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            # Si las credenciales de inicio de sesión son incorrectas, renderiza el template 'signin.html' con un mensaje de error
            return render(request, 'signin.html', {
                'title': 'Iniciar Sesión',
                'error': 'Usuario o contraseña incorrectos'
            })
        last_login = user.last_login
        login(request, user)

        if last_login is None:
            # Si es el primer inicio de sesión del usuario, redirige a la página de cambio de contraseña
            return redirect('change_pass')

        # Si el usuario ya ha iniciado sesión anteriormente, redirige al panel de control
        return redirect('dashboard')

    # Renderiza el template 'signin.html' para mostrar el formulario de inicio de sesión
    return render(request, 'signin.html', {
        'login': True,
        'title': 'Iniciar Sesión'
    })

@login_required
def administrators(request):
    # Obtiene todos los administradores y los pasa como contexto al template 'admins.html'
    admins = Administrator.objects.all()
    return render(request, 'admins.html', {
        'title': 'Administradores',
        'admins': admins,
        'panel': 'Administradores'
    })

@login_required
def delete_admin(request, id):
    admin = get_administrator(id)
    if admin:
        # Elimina el administrador y redirige a la lista de administradores
        admin.delete()
        return redirect('admins')
    else:
        # Si el administrador no existe, muestra un mensaje de error al usuario
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'El administrador no existe.'
        })

@login_required
def edit_admin(request, id):
    admin = get_administrator(id)
    if not admin:
        # Si el administrador no existe, muestra un mensaje de error al usuario
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'El administrador no existe.'
        })

    form = EditAdminForm(request.POST or None, initial={
        'username': admin.username,
        'email': admin.email,
        'name': admin.name,
        'lastname': admin.last_name
    })

    if request.method == 'POST':
        if form.is_valid():
            # Actualiza los datos del administrador con los valores del formulario y guarda los cambios
            admin.username = form.cleaned_data['username']
            admin.email = form.cleaned_data['email']
            admin.name = form.cleaned_data['name']
            admin.last_name = form.cleaned_data['lastname']
            admin.save()
            return redirect('dashboard')

    # Renderiza el template 'editadmin.html' con el formulario y los datos del administrador
    return render(request, 'editadmin.html', {
        'title': 'Editar administrador',
        'form': form
    })

@login_required
def change_pass(request):
    form = ChangePassForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            id = request.POST.get('id')
            admin = get_administrator(id)
            if not admin:
                # Si el administrador no existe, muestra un mensaje de error al usuario
                return render(request, 'error.html', {
                    'title': 'Error',
                    'message': 'El administrador no existe.'
                })
            # Cambia la contraseña del administrador y guarda los cambios
            admin.set_password(form.cleaned_data['password1'])
            admin.save()
            return redirect('dashboard')

    # Renderiza el template 'changepass.html' con el formulario de cambio de contraseña
    return render(request, 'changepass.html', {
        'title': 'Cambiar contraseña',
        'form': form
    })

@login_required
def create_admin(request):
    if request.method == 'POST':
        form = CreateAdminForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['lastname']
            password = form.cleaned_data['password1']

            is_superuser = bool(form.cleaned_data.get('superuser', False))
            if is_superuser:
                # Crea un nuevo administrador con privilegios de superusuario y guarda el objeto
                admin = Administrator.objects.create_superuser(
                    email=email,
                    username=username,
                    name=name,
                    last_name=last_name,
                    password=password
                )
            else:
                # Crea un nuevo administrador sin privilegios de superusuario y guarda el objeto
                admin = Administrator.objects.create_user(
                    email=email,
                    username=username,
                    name=name,
                    last_name=last_name,
                    password=password
                )

            admin.save()
            return redirect('admins')
    else:
        form = CreateAdminForm()

    # Renderiza el template 'createadmin.html' con el formulario de creación de administrador
    return render(request, 'createadmin.html', {
        'title': 'Agregar administrador',
        'form': form
    })

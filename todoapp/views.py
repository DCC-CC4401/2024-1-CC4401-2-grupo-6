from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.
from todoapp.models import Tarea
from todoapp.models import User  

from categorias.models import Categoria

from todoapp.forms import NuevaTareaModelForm


def tareas(request): #the index view
    #mis_tareas = Tarea.objects.all()  # quering all todos with the object manager
    if request.user.is_authenticated:
        mis_tareas = Tarea.objects.filter(owner=request.user)# quering all todos with the object manager
    else:
       mis_tareas = Tarea.objects.filter(owner=None)

    categorias = Categoria.objects.all()  # getting all categories with object manager
    
    if request.method == "GET":
        form_tarea = NuevaTareaModelForm()
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "form_tarea":form_tarea})

    if request.method == "POST":
        form_tarea= NuevaTareaModelForm(request.POST)
        if form_tarea.is_valid():
            
            if request.user.is_authenticated: # si el usuario está registrado
                nueva_tarea = form_tarea.save(commit=False)
                nueva_tarea.owner = request.user
                nueva_tarea.clean()

                if Tarea.objects.count() >= 5: # Si hay 5 tareas o más
                    messages.error(request, 'No puedes tener más de 5 solicitudes activas.')
                    return redirect('/tareas')
                
                # Si hay menos de 5 tareas, se guarda la nueva tarea
                nueva_tarea.save() 
                messages.success(request, 'Se subió la solicitud correctamente para: ' + nueva_tarea.titulo)
                

            else: # Si el usuario no está autenticado
                # Añadir mensaje de error
                messages.error(request, 'Debes estar registrado para poder enviar una solicitud.')
                return redirect('/tareas')

        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "form_tarea": form_tarea})

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
     return render(request, "todoapp/register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
     #Tomar los elementos del formulario que vienen en request.POST
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     apodo = request.POST['apodo']
     pronombre = request.POST['pronombre']
     mail = request.POST['mail']

     #Crear el nuevo usuario
     user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo, pronombre=pronombre)
     messages.success(request, 'Se creó el usuario para ' + user.apodo)

     #Redireccionar la página /tareas
     return HttpResponseRedirect('/tareas')

def login_user(request):
    if request.method == 'GET':
        return render(request,"todoapp/login.html")  
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/tareas')
        else:
            return HttpResponseRedirect('/register')

 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

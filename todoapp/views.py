# Create your views here.
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.
from todoapp.models import Tarea
from todoapp.models import User  
from .models import Bathroom
from .forms import BathroomForm

from categorias.models import Categoria

from todoapp.forms import NuevaTareaModelForm

def home(request):
    # Filtrar baños que estén marcados como publicados
    bathrooms = Bathroom.objects.filter(publicar=True)
    
    # Obtener opciones de filtrado y listas para la interfaz
    buildings = Bathroom.objects.values_list('building', flat=True).distinct()
    floors = Bathroom.objects.values_list('floor', flat=True).distinct().order_by('floor')
    genders = [choice[0] for choice in Bathroom.GENDER_CHOICES]
    
    # Aplicar filtros si se reciben en la solicitud GET
    building_filter = request.GET.get('building')
    floor_filter = request.GET.get('floor')
    bathroom_filter = request.GET.get('bathroom')
    gender_filter = request.GET.get('gender')

    if building_filter:
        bathrooms = bathrooms.filter(building=building_filter)
    
    if floor_filter:
        bathrooms = bathrooms.filter(floor=floor_filter)

    if bathroom_filter:
        bathrooms = bathrooms.filter(name=bathroom_filter)

    if gender_filter:
        bathrooms = bathrooms.filter(gender=gender_filter)

    # Obtener nombres de baños disponibles
    available_bathrooms = bathrooms.values_list('name', flat=True)

    context = {
        'bathrooms': bathrooms,
        'buildings': buildings,
        'floors': floors,
        'available_bathrooms': available_bathrooms,
        'genders': genders,
        'selected_building': building_filter,
        'selected_floor': floor_filter,
        'selected_bathroom': bathroom_filter,
        'selected_gender': gender_filter,
    }
    return render(request, 'todoapp/home.html', context)

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
     #pronombre = request.POST['pronombre']
     mail = request.POST['mail']

     #Crear el nuevo usuario
     user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo)
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
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/register')

 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

def forgot_password(request):
    """
    This function is called when the user wants to recover their password on the
    login page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is 'GET', it renders the 'forgot_password.html' template.
    - If the request method is 'POST', it retrieves the email from the request data,
      checks if a user with that email exists, and redirects the user accordingly.
      If the user exists, a success message is displayed and the user is redirected
      to the '/tareas' URL. Otherwise, the user is redirected to the '/register' URL.

    """
    if request.method == 'GET':
        return render(request, "todoapp/forgot_password.html")
    if request.method == 'POST':
        mail = request.POST['mail']
        usuario = User.objects.get(email=mail)
        if usuario is not None:
            messages.success(request, 'Se envió un correo a ' + usuario.email)
            return HttpResponseRedirect('/tareas')
        else:
            return HttpResponseRedirect('/register')
        

def bathroom_list(request):
    # Filtrar baños que estén marcados como publicados
    bathrooms = Bathroom.objects.filter(publicar=True)
    
    # Obtener opciones de filtrado y listas para la interfaz
    buildings = Bathroom.objects.values_list('building', flat=True).distinct()
    floors = Bathroom.objects.values_list('floor', flat=True).distinct().order_by('floor')
    genders = [choice[0] for choice in Bathroom.GENDER_CHOICES]
    
    # Aplicar filtros si se reciben en la solicitud GET
    building_filter = request.GET.get('building')
    floor_filter = request.GET.get('floor')
    bathroom_filter = request.GET.get('bathroom')
    gender_filter = request.GET.get('gender')

    if building_filter:
        bathrooms = bathrooms.filter(building=building_filter)
    
    if floor_filter:
        bathrooms = bathrooms.filter(floor=floor_filter)

    if bathroom_filter:
        bathrooms = bathrooms.filter(name=bathroom_filter)

    if gender_filter:
        bathrooms = bathrooms.filter(gender=gender_filter)

    # Obtener nombres de baños disponibles
    available_bathrooms = bathrooms.values_list('name', flat=True)

    context = {
        'bathrooms': bathrooms,
        'buildings': buildings,
        'floors': floors,
        'available_bathrooms': available_bathrooms,
        'genders': genders,
        'selected_building': building_filter,
        'selected_floor': floor_filter,
        'selected_bathroom': bathroom_filter,
        'selected_gender': gender_filter,
    }
    return render(request, 'todoapp/bathroom_list.html', context)

def bathroom_detail(request, id):
    bathroom = Bathroom.objects.get(id=id)
    return render(request, 'todoapp/bathroom_detail.html', {'bathroom': bathroom})

def add_bathroom(request):
    if request.method == 'POST':
        form = BathroomForm(request.POST)
        if form.is_valid():
            # guardar form para que un admin marque true en la pagina de admin posteriormente
            bathroom = form.save(commit=False)
            bathroom.publicar = False  # Marcar como no revisado por defecto
            form.save() # Guarda los datos en la base de datos si el formulario es válido
            #return redirect('bathroom_list')  # Redirige a alguna otra vista o página
            messages.success(request, 'El baño se ha agregado correctamente.')
            return redirect('home') 
    else:
        form = BathroomForm()

    return render(request, 'todoapp/add_bathroom.html', {'form': form})

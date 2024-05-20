#user: wcadmin
#mail: wcadmin@uchile.cl
#pass: wcadmin

from django.contrib import admin
from todoapp.models import  User, Tarea
#from categorias.models import Categoria

#admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Tarea)

# Register your models here.

# Importamos modulos necesarios
from django.db import models
from django.utils import timezone
from categorias.models import Categoria
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg

# Creamos la clase User que hereda de AbstractUser
# para agregar campos personalizados al modelo User
# pronombre y apodo, los pronombres se eliminaron del proyecto
class User(AbstractUser):
  pronombres = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pronombre = models.CharField(max_length=5,choices=pronombres)
  apodo = models.CharField(max_length=30)
    
# Creamos la clase Tarea que hereda de models.Model
# para crear los campos a pedir en la creación del formulario de baño
# esto no se uso en el proyecto
class Tarea(models.Model):  # Todolist able name that inherits models.Model
    titulo = models.CharField(max_length=250)  # un varchar
    contenido = models.TextField(blank=True)  # un text
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # un date
    categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea
    owner = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo  # name to be shown when called

# Creamos la clase Bathroom que hereda de models.Model
# para crear los campos a pedir en el formulario de baño
# este formulario se uso en el proyecto
# se pide el nombre, edificio, piso, género, descripción, imagen, publicar, latitud y longitud.
class Bathroom(models.Model):
    GENDER_CHOICES = [
        ('mujer', 'Mujer'),
        ('hombre', 'Hombre'),
        ('universal', 'Universal'),
    ]

    BUILDS_CHOICES = [
        ('850', '850'),
        ('851', '851'),
    ]

    FLOOR_CHOICES = [
        ('-3', '-3'),
        ('-2', '-2'),
        ('-1', '-1'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]

    name = models.CharField(max_length=100)

    building = models.CharField(max_length=3, choices=BUILDS_CHOICES)

    floor = models.CharField(max_length=2,choices=FLOOR_CHOICES)
            
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    description = models.CharField(max_length=300)

    image = models.ImageField(upload_to='bathroom_images/', blank=True, null=True)

    # el formulario debe ser aceptado por un admin
    publicar = models.BooleanField(default=False)  
    # agregar por el admin
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Edificio {self.building}, Piso {self.floor}, {self.get_gender_display()}"
    
    def average_cleaning_points(self):
        average = self.cleaning_reviews.aggregate(Avg('points'))['points__avg']
        return average
    
    def print_test(self):
        return self.cleaning_reviews.all()

# Creamos la clase Comment que hereda de models.Model
# para crear los campos a pedir en el formulario de comentarios
# los comentarios se publican estando la sesión iniciada
class Comment(models.Model):
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.bathroom.name}"

# Creamos la clase Cleaning que hereda de models.Model
# para crear los campos a pedir en el formulario de limpieza
# los puntos se asignan desde el 1 al 10
class Cleaning(models.Model):
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE, related_name='cleaning_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points= models.IntegerField()
    def __str__(self):
        return f"{self.user.username} calificó con {self.points} el baño{self.bathroom.name} "
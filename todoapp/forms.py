from django import forms
from .models import Cleaning, Tarea
from .models import Bathroom
from .models import Comment
from categorias.models import Categoria

class NuevaTareaModelForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'contenido', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Baño DCC Torre Norte Tercer Piso Mujeres'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Buena señal de wifi, limpio, posee perfumadores en cada cabina, etc.'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_titulo(self):
        field = self.cleaned_data.get("titulo")
        if not "Baño" in field:
            raise forms.ValidationError("Debe incluir el texto 'Baño' en el título")
        return field

class BathroomForm(forms.ModelForm):
    cleaning_points = forms.IntegerField(
        label='Limpieza',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 10,
            'placeholder': 'Ingrese un número del 1 al 10'
        }))
    class Meta:
        model = Bathroom
        fields = ['name', 'building', 'floor', 'gender', 'description', 'image']
        labels = {
            'name': 'Nombre',
            'building': 'Edificio',
            'floor': 'Piso',
            'gender': 'Género',
            'description': 'Descripción',
            'image': 'Foto'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Baño'}),
            'building': forms.Select(attrs={'class': 'form-control'}),
            'floor': forms.Select(attrs={'class': 'form-control'}), 
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indique como llegar al baño y detalles importantes, Ej: Baño amplio, etc.'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Comentario',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Fui al baño y la luz estaba mala, etc.'}),
        }

class CleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['points']
        label ={
            'points':'puntos'
        }
        widgets = {'content': forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 10
        })}
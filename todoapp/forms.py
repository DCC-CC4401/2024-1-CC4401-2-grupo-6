from django import forms
from .models import Tarea
from .models import Bathroom
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
    class Meta:
        model = Bathroom
        fields = ['name', 'building', 'floor', 'gender', 'description']
        labels = {
            'name': 'Nombre',
            'building': 'Edificio',
            'floor': 'Piso',
            'gender': 'Género',
            'description': 'Descripción',
            'image': 'Foto'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'building': forms.Select(attrs={'class': 'form-control'}),
            'floor': forms.Select(attrs={'class': 'form-control'}), 
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
from django import forms
from .models import Tarea
from categorias.models import Categoria

class NuevaTareaModelForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'contenido', 'categoria']

    def clean_titulo(self):	
        field = self.cleaned_data.get("titulo")
        if not "Tarea" in field:
            raise forms.ValidationError("Debe incluir el texto 'Tarea'")
        return field
from django import forms
from .models import Poster

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['titulo','precio','etiqueta','imagen']
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titulo'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Precio'}),
            'etiqueta' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Etiqueta'}),
        }
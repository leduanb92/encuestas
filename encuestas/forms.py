from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets

from encuestas.models import Encuesta


class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(attrs={'class': 'form-control'}),
            'edad': widgets.NumberInput(attrs={'class': 'form-control', 'min': 10, 'max': 130}),
            'peso_corporal': widgets.NumberInput(attrs={'class': 'form-control', 'min': 20}),
            'sexo': widgets.Select(attrs={'class': 'form-select'}),
            'grado_de_escolaridad': widgets.Select(attrs={'class': 'form-select'}),
            'intereses_personales': widgets.CheckboxSelectMultiple(),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre.split()) < 3:
            raise ValidationError('Debe especificar su nombre completo, incluyendo ambos apellidos')
        return nombre.title()

    def clean_peso_corporal(self):
        peso = self.cleaned_data['peso_corporal']
        if peso <= 0:
            raise ValidationError('El peso debe ser un valor positivo')
        return peso

    def clean_edad(self):
        # Como no se especifica establecí un rango lo más lógico posible.
        edad = self.cleaned_data['edad']
        if edad < 10:
            raise ValidationError('Su edad debe ser mayor a 10 años')
        if edad > 130:
            raise ValidationError('Su edad debe ser menor a 130 años')
        return edad

from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona # modelo o tabla
        fields = '__all__' # campos que queremos
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        } # Tipo de campo, podemos especificar el tipo de dato a nivel de html que va a tener cada uno de nuestros campos

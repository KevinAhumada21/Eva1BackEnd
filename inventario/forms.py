from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if '@' not in correo or not correo.endswith(('.com', '.cl')):
            raise forms.ValidationError("Correo inválido, debe cumplir con el formato correcto.")
        return correo


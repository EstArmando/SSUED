from django import forms
from .models import Disability

class DisabilityForm(forms.Form):
    type = forms.CharField(
        label='Discapacidad',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la discapacidad'}),
        required=True
    )

    def clean_type(self):
        type = self.cleaned_data['type']
        if not type.strip():
            raise forms.ValidationError('El campo de discapacidad no puede estar vacío.')
        if Disability.objects.filter(type=type).exists():
            raise forms.ValidationError('La discapacidad ya existe en la base de datos.')
        return type



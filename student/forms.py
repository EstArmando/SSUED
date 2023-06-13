from django import forms
from django.core.exceptions import ValidationError

from student.models import Sex
from university.models import University
from disability.models import Disability

class StudentForm(forms.Form):
    age = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su edad'}),
        required=True,
        error_messages={
            'required': 'El campo de edad es requerido',
            'invalid': 'Ingrese un número válido para la edad',
        }
    )

    admission_year = forms.IntegerField(
        label='Año de Ingreso',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el año de ingreso'}),
        required=True,
        error_messages={
            'required': 'El campo de año de ingreso es requerido',
            'invalid': 'Ingrese un número válido para el año de ingreso',
        }
    )

    gender = forms.ModelChoiceField(
        label='Sexo',
        queryset=Sex.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    university = forms.ModelChoiceField(
        label='Universidad',
        queryset=University.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    disability = forms.ModelChoiceField(
        label='Discapacidad',
        queryset=Disability.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not age:
            raise ValidationError('El campo de edad es requerido')
        return age

    def clean_admission_year(self):
        admission_year = self.cleaned_data.get('admission_year')
        if not admission_year:
            raise ValidationError('El campo de año de ingreso es requerido')
        return admission_year
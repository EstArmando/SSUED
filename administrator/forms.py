from django import forms
from django.core.validators import validate_email
from .models import Administrator


class CreateAdminForm(forms.Form):
    # Campo de formulario para el nombre de usuario
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su usuario'}),
        required=True
    )

    # Campo de formulario para el correo electrónico
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico'}),
        required=True,
        error_messages={
            'invalid': 'Ingrese una dirección de correo electrónico válida.',
        }
    )

    # Campo de formulario para el nombre
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
        required=False
    )

    # Campo de formulario para el apellido
    lastname = forms.CharField(
        label='Apellido',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
        required=False
    )

    # Campo de formulario para la contraseña
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}),
        required=True
    )

    # Campo de formulario para confirmar la contraseña
    password2 = forms.CharField(
        label='Confirme contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme la contraseña'}),
        required=True
    )

    # Campo de formulario para el superusuario (opcional)
    superuser = forms.BooleanField(label='Superusuario', required=False)

    def clean_username(self):
        # Validación personalizada para el nombre de usuario
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('El nombre de usuario es requerido')
        if Administrator.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya está en uso')
        return username

    def clean_email(self):
        # Validación personalizada para el correo electrónico
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('El correo electrónico es requerido')
        validate_email(email)
        if Administrator.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya está en uso')
        return email

    def clean_password1(self):
        # Validación personalizada para la contraseña
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError('La contraseña es requerida')
        return password1

    def clean_password2(self):
        # Validación personalizada para confirmar la contraseña
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError('La confirmación de contraseña es requerida')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


class EditAdminForm(forms.Form):
    # Campo de formulario para el nombre de usuario (opcional)
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su usuario'}),
        required=False
    )

    # Campo de formulario para el correo electrónico (opcional)
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico'}),
        required=False,
        error_messages={
            'invalid': 'Ingrese una dirección de correo electrónico válida.',
        }
    )

    # Campo de formulario para el nombre (opcional)
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
        required=False
    )

    # Campo de formulario para el apellido (opcional)
    lastname = forms.CharField(
        label='Apellido',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
        required=False
    )

    def clean_username(self):
        # Validación personalizada para el nombre de usuario al editarlo
        username = self.cleaned_data.get('username')
        if username and username != self.initial.get('username') and Administrator.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya está en uso')
        if not username:
            raise forms.ValidationError('El nombre de usuario es requerido')
        return username

    def clean_email(self):
        # Validación personalizada para el correo electrónico al editarlo
        email = self.cleaned_data.get('email')
        if email and email != self.initial.get('email') and Administrator.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya está en uso')
        if not email:
            raise forms.ValidationError('El correo electrónico es requerido')
        validate_email(email)
        return email


class ChangePassForm(forms.Form):
    # Campo de formulario para la contraseña
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}),
        required=True
    )

    # Campo de formulario para confirmar la contraseña
    password2 = forms.CharField(
        label='Confirme contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme la contraseña'}),
        required=True
    )

    def clean_password1(self):
        # Validación personalizada para la contraseña al cambiarla
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError('La contraseña es requerida')
        return password1

    def clean_password2(self):
        # Validación personalizada para confirmar la contraseña al cambiarla
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError('La confirmación de contraseña es requerida')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

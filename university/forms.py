from django import forms


class UniversityForm(forms.Form):
    code = forms.CharField(
        label='Codigo',
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el codigo'}),
        required=True
    )
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la universidad'}),
        required=True
    )
    acronyms = forms.CharField(
        label='Siglas',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las siglas de la universidad'}),
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        name = cleaned_data.get('name')
        acronyms = cleaned_data.get('acronyms')

        if not code:
            self.add_error('code', 'Este campo es obligatorio.')
        if not name:
            self.add_error('name', 'Este campo es obligatorio.')
        if not acronyms:
            self.add_error('acronyms', 'Este campo es obligatorio.')

        return cleaned_data

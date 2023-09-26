from django import forms
from django.forms import TextInput

from aplicatieTicketing.models import Registration


class RegistrationClass(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'id_user', 'password',
                  'confirm_password', 'email', 'telephone']

    widgets = {
        'first_name': TextInput(attrs={'placeholder': "First name", 'class': 'form-control'}),
        'last_name': TextInput(attrs={'placeholder': "Last name", 'class': 'form-control'}),
        'id_user': TextInput(attrs={'placeholder': "ID user", 'class': 'form-control'}),
        'password': TextInput(attrs={'placeholder': "Password", 'class': 'form-control'}),
        'confirm_password': TextInput(attrs={'placeholder': "Confirm password", 'class': 'form-control'}),
        'email': TextInput(attrs={'placeholder': "E-mail", 'class': 'form-control'}),
        'telephone': TextInput(attrs={'placeholder': "E-mail", 'class': 'form-control'}),
    }

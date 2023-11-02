from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput


# class NewAccountForm(forms.ModelForm):
class NewAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username')

        labels = {"last_name": "Nume", "first_name": "Prenume", "email": "Email",
                  "username": "Nume utilizator", "password1": "Parola"}

        widgets = {
            'last_name': TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'placeholder': 'Prenume', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-control'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Parola', 'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'placeholder': 'Confirma parola', 'class': 'form-control'})
        self.fields['password1'].label = 'Parola'
        self.fields['password2'].label = 'Confirma parola'
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        # username_value = field_data.get('username')
        # if User.objects.filter(username__iexact=username_value).exists():
        #         self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
        # if User.objects.filter(username=username_value).exists():
        #         self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        return field_data

    def clean_username(self):
        field_data = self.cleaned_data
        username_value = field_data.get('username')
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        return field_data


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username')

        labels = {"last_name": "Nume", "first_name": "Prenume", "email": "Email",
                  "username": "Nume utilizator", "password1": "Parola"}

        widgets = {
            'last_name': TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'placeholder': 'Prenume', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-control'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(EditAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if self.pk:
            if User.objects.filter(email=email_value).exclude(id=self.pk).exists():
                self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
            if User.objects.filter(username=username_value).exclude(id=self.pk).exists():
                self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        else:
            if User.objects.filter(email=email_value).exists():
                self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
            if User.objects.filter(username=username_value).exists():
                self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        return field_data

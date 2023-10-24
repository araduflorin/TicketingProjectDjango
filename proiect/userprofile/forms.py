from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput


# class NewAccountForm(forms.ModelForm):
class NewAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Prenume', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Nume utilizator', 'class': 'form-control'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if self.pk:
            if User.objects.filter(email__icontains=email_value).exclude(id=self.pk).exists():
                self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
            if User.objects.filter(username__icontains=username_value).exclude(id=self.pk).exists():
                self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        else:
            if User.objects.filter(email__icontains=email_value).exists():
                self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
            if User.objects.filter(username__icontains=username_value).exists():
                self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        return field_data

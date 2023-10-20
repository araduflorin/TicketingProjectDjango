from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput


# class NewAccountForm(forms.ModelForm):
class NewAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','username')

        widgets = {
            'first_name':TextInput(attrs={'placeholder':'Prenume','class':'form-control'}),
            'last_name':TextInput(attrs={'placeholder':'Nume','class':'form-control'}),
            'email':EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            'username':TextInput(attrs={'placeholder':'Username','class':'form-control'}),
            # 'password1':forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}),
            # 'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control'}),
            # 'password1':forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})),
            # 'password2':forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})),

        }

    def __init__(self,*args,**kwargs):
        super(NewAccountForm,self).__init__(*args,**kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder':'Password','class':'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder':'Password','class':'form-control'})

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            msg = 'Emailul deja exista! Te rugam sa adaugi alt email!'
            self._errors['email'] = self.error_class([msg])
        if User.objects.filter(username=username_value).exists():
            msg = 'Username-ul exista! Te rugam sa alegi altul!'
            self._errors['username'] = self.error_class([msg])
        return field_data
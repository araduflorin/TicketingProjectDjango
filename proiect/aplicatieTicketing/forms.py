from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, CharField, PasswordInput, Select, ChoiceField

from aplicatieTicketing.models import Contact, Ticket, Status, Type
from aplicatieTicketing.models import Contact, Ticket


#
# "Vă rugăm să introduceți un nume de utilizator și o parolă corecte." \
#              " Rețineți că ambele câmpuri pot fi sensibile la majuscule."

class ContactClass(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        labels = {"name": "Nume", "email": "Email", "message": "Mesaj"}

    widgets = {
        'name': TextInput(attrs={'placeholder': "Name", 'class': 'form-control'}),
        'email': TextInput(attrs={'placeholder': "E-mail", 'class': 'form-control'}),
        'message': TextInput(attrs={'placeholder': "Message", 'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(ContactClass, self).__init__(*args, **kwargs)


class TicketClass(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject_ticket', 'type', 'status', 'description']

        labels = {"subject_ticket": "Subiect tichet", "type": "Tip tichet", "status": "Stare tichet",
                  "description": "Descriere"}

        widgets = {
            'subject_ticket': TextInput(attrs={'class': 'form-control', 'style': 'height:32px'}),
            'type': Select(attrs={'class': 'form-control', 'style': 'height:32px'}),
            'status': Select(attrs={'df-show':".name=='Modifica'",'class': 'form-control', 'style': 'height:32px'}),
            'description': TextInput(attrs={'class': 'form-control', 'style': 'height:32px'}),
            # 'email': TextInput(attrs={'class': 'form-control', 'style': 'height:32px'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(TicketClass, self).__init__(*args, **kwargs)

        # superusers = User.objects.filter(is_superuser=True)
        # if not superusers:
        # self.fields['status'].choices = [("10", "Trimis")]
        # self.fields['status'].initial = 'Trimis'
        # self.fields['status'].widget = forms.HiddenInput()
        # self.label_suffix[-2].widget = forms.HiddenInput()

        self.fields['type'].empty_label = ""
        self.fields['type'].size = "200"
        # self.fields['status'].widget = Select(attrs={'placeholder': "Stare", 'class': 'form-control'}),
        # self.fields['type'].widget = ChoiceField(choices={'placeholder': "Tip", 'class': 'form-control'}),
        # self.fields['status'].widget.attrs['placeholder'] = 'Stare'
        self.pk = pk


    def clean(self):
        name_value = self.cleaned_data.get('subject_ticket')
        if self.pk:
            if Ticket.objects.filter(subject_ticket__icontains=name_value).exclude(id=self.pk).exists():
                self._errors['subject_ticket'] = self.error_class(['Subiectul introdus deja exista'])
        else:
            if Ticket.objects.filter(subject_ticket__icontains=name_value).exists():
                self._errors['subject_ticket'] = self.error_class(['Subiectul introdus deja exista'])
        return self.cleaned_data


class StatusTicket(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'description']

        widgets = {
            'name': TextInput(attrs={'placeholder': "Nume", 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': "Descriere", 'class': 'form-control'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(StatusTicket, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        name_value = self.cleaned_data.get('name')
        if self.pk:
            if Status.objects.filter(name__icontains=name_value).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Starea introdusa deja exista'])
        else:
            if Status.objects.filter(name__icontains=name_value).exists():
                self._errors['name'] = self.error_class(['Starea introdusa deja exista'])
        return self.cleaned_data


class TypeTicket(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name', 'description']

        widgets = {
            'name': TextInput(attrs={'placeholder': "Nume", 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': "Descriere", 'class': 'form-control'}),

        }

    def __init__(self, pk, *args, **kwargs):
        super(TypeTicket, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nume tip tichet"
        self.fields['description'].label = "Descriere tip tichet"
        self.pk = pk

    def clean(self):
        name_value = self.cleaned_data.get('name')
        if self.pk:
            if Type.objects.filter(name__icontains=name_value).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Tipul introdus deja exista'])
        else:
            if Type.objects.filter(name__icontains=name_value).exists():
                self._errors['name'] = self.error_class(['Tipul introdus deja exista'])
        return self.cleaned_data

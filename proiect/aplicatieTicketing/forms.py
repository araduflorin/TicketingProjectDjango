from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, CharField, PasswordInput

from aplicatieTicketing.models import Contact, Ticket, Status, Type
from aplicatieTicketing.models import Contact, Ticket


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
        fields = ['subject_ticket', 'status', 'type', 'name',
                  'email']

        labels = {"subject_ticket": "Subiect tichet", "status": "Stare", "type": "Tip tichet",
                  "name": "Nume utilizator", "email": "Email"}

    widgets = {
        'subject_ticket': TextInput(attrs={'placeholder': "Subiect", 'class': 'form-control'}),
        'status': TextInput(attrs={'placeholder': "Stare", 'class': 'form-control'}),
        'type': TextInput(attrs={'placeholder': "Tip", 'class': 'form-control'}),
        'name': TextInput(attrs={'placeholder': "Nume", 'class': 'form-control'}),
        'email': TextInput(attrs={'placeholder': "Email", 'class': 'form-control'}),


    }

    def __init__(self, pk, *args, **kwargs):
        super(TicketClass, self).__init__(*args, **kwargs)
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


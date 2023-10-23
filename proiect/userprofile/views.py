from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from userprofile.forms import NewAccountForm


# Create your views here.
class CreateNewAccountView(CreateView):
    model = User
    form_class = NewAccountForm
    template_name = 'aplicatieTicketing/registration_form.html'

    def get_form_kwargs(self, **kwargs):
        data = super(CreateNewAccountView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:login')


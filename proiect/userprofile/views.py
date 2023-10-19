from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from userprofile.forms import NewAccountForm


# Create your views here.
class CreateNewAccountView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'aplicatieTicketing/registration_form.html'
    form_class = NewAccountForm

    def get_success_url(self):
        return reverse('aplicatieTicketing:generalHtml')
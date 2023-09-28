from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView

from aplicatieTicketing.forms import RegistrationClass, ContactClass
from aplicatieTicketing.models import Registration, Contact


# Create your views here.
# class GeneralView:
#     template_name = 'aplicatieTicketing/general_index.html'

class CreateRegistrationView(CreateView):
    model = Registration
    # fields = ['first_name', 'last_name', 'id_user']
    form_class = RegistrationClass
    template_name = 'aplicatieTicketing/registration_form.html'

    def get_success_url(self):
        return reverse('aplicatieTicketing:general')

class CreateContactView(CreateView):
    model = Contact
    form_class = ContactClass
    template_name = 'aplicatieTicketing/contact_form.html'

def general(request):
  template_name = loader.get_template('aplicatieTicketing/general_index.html')
  return HttpResponse(template_name.render())
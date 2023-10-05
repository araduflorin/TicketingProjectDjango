from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView

from aplicatieTicketing.forms import RegistrationClass, ContactClass, TicketClass
from aplicatieTicketing.models import Registration, Contact, Ticket


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

@login_required
def user(request):
  template_name = loader.get_template('aplicatieTicketing/user_form.html')
  return HttpResponse(template_name.render())


class CreateTicket(CreateView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form.html'

    def general(request):
        template_name = loader.get_template('aplicatieTicketing/general_index.html')
        return HttpResponse(template_name.render())
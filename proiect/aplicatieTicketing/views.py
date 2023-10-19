from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView, ListView


from aplicatieTicketing.forms import RegistrationClass, ContactClass, TicketClass, TypeTicket, StatusTicket
from aplicatieTicketing.models import Contact, Ticket, Type, Status, Registration

from aplicatieTicketing.forms import RegistrationClass, ContactClass, TicketClass, TicketTypeClass
from aplicatieTicketing.models import Contact, Ticket, TicketType



# Create your views here.
# class GeneralView:
#     template_name = 'aplicatieTicketing/general_index.html'

class CreateRegistrationView(CreateView):
    model = Registration
    # fields = ['first_name', 'last_name', 'id_user']
    form_class = RegistrationClass
    template_name = 'aplicatieTicketing/registration_form.html'

    def get_success_url(self):
        return reverse('aplicatieTicketing:generalHtml')


# def all_users(request):
#     list_users = Registration.objects.all()
#     return render(request, 'aplicatieTicketing/user_form.html',{ 'users':list_users })

class CreateContactView(CreateView):
    model = Contact
    form_class = ContactClass
    template_name = 'aplicatieTicketing/contact_form.html'


def general(request):
    template_name = loader.get_template('aplicatieTicketing/general_index.html')
    return HttpResponse(template_name.render())


# @login_required
# def user(request):
#   template_name = loader.get_template('aplicatieTicketing/user_form.html')
#   return HttpResponse(template_name.render())


class CreateTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form.html'


    def form_valid(self, form):
        if form.is_valid():
            ticket_instance = form.save(commit=False)
            ticket_instance.user_id = self.request.user.id
            ticket_instance.save()
        return super(CreateTicket, self).form_valid(form)

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')

    # def get_form_kwargs(self):
    #     data = super(CreateTicket,self).get_form_kwargs()
    #     data.update({'pk': None})
    #     return data


class ViewTicket(LoginRequiredMixin, ListView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form_list.html'
    context_object_name = 'ticket'

    def get_context_data(self, *args, **kwargs):
        data = super(ViewTicket, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_ticket'] = Ticket.objects.all()
        else:
            data['all_ticket'] = Ticket.objects.filter(user_id=self.request.user.id)
        return data


class ListofUsersList(LoginRequiredMixin, ListView):
    model = Registration
    form_class = RegistrationClass
    template_name = 'aplicatieTicketing/user_form.html'
    context_object_name = 'users'


class CreateTypeTicket(LoginRequiredMixin, CreateView):
    model = Type
    form_class = TypeTicket
    template_name = 'aplicatieTicketing/type_ticket.html'

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')


class CreateStatusTicket(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusTicket
    template_name = 'aplicatieTicketing/status_ticket.html'

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')

    def general(request):
        template_name = loader.get_template('aplicatieTicketing/general_index.html')
        return HttpResponse(template_name.render())


class CreateTicketType(CreateView):
    model = TicketType
    form_class = TicketTypeClass
    template_name = 'aplicatieTicketing/ticket_type_form.html'
    context_object_name = 'type_ticket'

    def get_success_url(self):
        return reverse('aplicatieTicketing:list_type_ticket')


class TicketTypeView(ListView):
    model = TicketType
    form_class = TicketTypeClass
    template_name = 'aplicatieTicketing/ticket_type_index.html'
    context_object_name = 'type_ticket'



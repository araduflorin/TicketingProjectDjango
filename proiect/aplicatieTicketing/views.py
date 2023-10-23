from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, request
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView, ListView, FormView, UpdateView

from aplicatieTicketing.forms import RegistrationClass, ContactClass, TicketClass
from aplicatieTicketing.forms import TypeTicket, StatusTicket
from aplicatieTicketing.models import Contact, Ticket
from aplicatieTicketing.models import Type, Status, Registration


class CreateContactView(CreateView):
    model = Contact
    form_class = ContactClass
    template_name = 'aplicatieTicketing/contact_form.html'


    def get_success_url(self):
        return reverse('aplicatieTicketing:success')

def success(request):
    template_name = loader.get_template('aplicatieTicketing/contact_succes.html')
    return HttpResponse(template_name.render())


class ViewContact(LoginRequiredMixin, ListView):
    model = Contact
    form_class = ContactClass
    template_name = 'aplicatieTicketing/contact_list.html'
    context_object_name = 'contact_list'


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

    def get_form_kwargs(self):
        data = super(CreateTicket, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def form_valid(self, form):
        if form.is_valid():
            ticket_instance = form.save(commit=False)
            ticket_instance.user_id = self.request.user.id
            ticket_instance.save()
        return super(CreateTicket, self).form_valid(form)

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')


class UpdateTicket(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form.html'

    def get_form_kwargs(self):
        data = super(UpdateTicket, self).get_form_kwargs()
        data.update({'pk':self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')


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

    def get_context_data(self, *args, **kwargs):
        data = super(ListofUsersList, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_users'] = User.objects.all()
        else:
            data['all_users'] = User.objects.filter(id=self.request.user.id)
        return data


class CreateTypeTicket(LoginRequiredMixin, CreateView):
    model = Type
    form_class = TypeTicket
    template_name = 'aplicatieTicketing/type_ticket.html'

    def get_form_kwargs(self):
        data = super(CreateTypeTicket, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:type_list')


class UpdateTypeTicket(LoginRequiredMixin, UpdateView):
    model = Type
    form_class = TypeTicket
    template_name = 'aplicatieTicketing/type_ticket.html'

    def get_form_kwargs(self):
        data = super(UpdateTypeTicket, self).get_form_kwargs()
        data.update({'pk':self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:type_list')

class ViewTypeTicket(LoginRequiredMixin, ListView):
    model = Type
    form_class = TypeTicket
    template_name = 'aplicatieTicketing/type_list.html'
    context_object_name = 'type_list'


class CreateStatusTicket(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusTicket
    template_name = 'aplicatieTicketing/status_ticket.html'

    def get_form_kwargs(self):
        data = super(CreateStatusTicket, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:status_list')


class UpdateStatusTicket(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusTicket
    template_name = 'aplicatieTicketing/status_ticket.html'

    def get_form_kwargs(self):
        data = super(UpdateStatusTicket, self).get_form_kwargs()
        data.update({'pk':self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:status_list')


class ViewStatusTicket(LoginRequiredMixin, ListView):
    model = Status
    form_class = StatusTicket
    template_name = 'aplicatieTicketing/status_list.html'
    context_object_name = 'status_list'


# class CreateTicketType(CreateView):
#     model = TicketType
#     form_class = TicketTypeClass
#     template_name = 'aplicatieTicketing/contact_list.html'
#     context_object_name = 'type_ticket'
#
#     def get_success_url(self):
#         return reverse('aplicatieTicketing:list_type_ticket')


# class TicketTypeView(ListView):
#     model = Type
#     form_class = TypeTicket
#     template_name = 'aplicatieTicketing/type_list.html'
#     context_object_name = 'type_ticket'


# class TicketStatusView(LoginRequiredMixin, ListView):
#     model = Status
#     form_class = StatusTicket
#     template_name = 'aplicatieTicketing/status_list.html'
#     context_object_name = 'st_ticket'

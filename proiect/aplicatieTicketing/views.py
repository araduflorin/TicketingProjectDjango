

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

from django.views.generic import CreateView, ListView, FormView, UpdateView

from aplicatieTicketing.forms import ContactClass, TicketClass
from aplicatieTicketing.forms import TypeTicket, StatusTicket
from aplicatieTicketing.models import Contact, Ticket
from aplicatieTicketing.models import Type, Status


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # messages.success(request, ("Logare reusita"))
            login(request, user)
            return redirect('aplicatieTicketing:ticket_inter')

        else:
            messages.success(request, ("A fost o eroare la logare, incearca din nou..."))
            return redirect('login')


    else:
        return render(request, 'registration/login.html', {})


class InterPageTicket(LoginRequiredMixin, ListView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_intermediar.html'
    context_object_name = 'ticket'

    def get_context_data(self, *args, **kwargs):
        data = super(InterPageTicket, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_ticket'] = Ticket.objects.all()
            data['count'] = Ticket.objects.all().count()
            data['count_final'] = Ticket.objects.filter(status=1).count()
            data['count_today'] = Ticket.objects.filter(created_at=datetime.now).count()
            # dat = datetime.now().today()
        else:
            data['all_ticket'] = Ticket.objects.filter(user_id=self.request.user.id)
            data['count'] = Ticket.objects.filter(user_id=self.request.user.id).count()
            data['count_final'] = Ticket.objects.filter(user_id=self.request.user.id, status=1).count()
            # data['count_today'] = Ticket.objects.filter(created_at=timezone.now()).count()
        return data


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
    template_name = loader.get_template \
        ('aplicatieTicketing/general_index.html')
    return HttpResponse(template_name.render())


# @login_required
# def user(request):
#   template_name = loader.get_template('aplicatieTicketing/user_form.html')
#   return HttpResponse(template_name.render())


class CreateTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CreateTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Adauga'
        return data

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

    def get_context_data(self, *args, **kwargs):
        data = super(UpdateTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Modifica'
        return data

    def get_form_kwargs(self):
        data = super(UpdateTicket, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:ticket_list')


class ViewTicket(LoginRequiredMixin, ListView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_form_list.html'
    # context_object_name = 'ticket'

    def get_context_data(self, *args, **kwargs):
        data = super(ViewTicket, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_ticket'] = Ticket.objects.all()
        else:
            data['all_ticket'] = Ticket.objects.filter(user_id=self.request.user.id)
        return data



class ListTicket(LoginRequiredMixin, ListView):
    model = Ticket
    form_class = TicketClass
    template_name = 'aplicatieTicketing/ticket_view.html'
    context_object_name = 'ticket'

    def get_context_data(self, *args, **kwargs):
        data = super(ListTicket, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_ticket'] = Ticket.objects.all()
            # data['count'] = Ticket.objects.all().count()
        else:
            data['all_ticket'] = Ticket.objects.filter(user_id=self.request.user.id)
            # data['count'] = Ticket.objects.filter(user_id=self.request.user.id).count()
        return data


# def count_ticket(request):
#     count = Ticket.objects.all().count()
#     context = {'count': count}
#     return render(request, 'aplicatieTicketing/ticket_view.html', context)


class CreateTypeTicket(LoginRequiredMixin, CreateView):
    model = Type
    form_class = TypeTicket
    template_name = 'aplicatieTicketing/type_ticket.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CreateTypeTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Adauga'
        return data

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

    def get_context_data(self, *args, **kwargs):
        data = super(UpdateTypeTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Modifica'
        return data

    def get_form_kwargs(self):
        data = super(UpdateTypeTicket, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
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

    def get_context_data(self, *args, **kwargs):
        data = super(CreateStatusTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Adauga'
        return data

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

    def get_context_data(self, *args, **kwargs):
        data = super(UpdateStatusTicket, self).get_context_data(*args, **kwargs)
        data['action'] = 'Modifica'
        return data

    def get_form_kwargs(self):
        data = super(UpdateStatusTicket, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatieTicketing:status_list')


class ViewStatusTicket(LoginRequiredMixin, ListView):
    model = Status
    form_class = StatusTicket
    template_name = 'aplicatieTicketing/status_list.html'
    context_object_name = 'status_list'


@login_required
def delete_status(request, pk):
    Status.objects.filter(id=pk).delete()
    return redirect('aplicatieTicketing:status_list')


@login_required
def delete_type(request, pk):
    Type.objects.filter(id=pk).delete()
    return redirect('aplicatieTicketing:type_list')

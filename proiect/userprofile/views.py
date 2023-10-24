from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

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


class UpdateAccountView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = NewAccountForm
    template_name = 'aplicatieTicketing/edit_user_form.html'

    def get_form_kwargs(self, **kwargs):
        data = super(UpdateAccountView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('userprofile:lista_utilizatori')

class ViewAccountList(LoginRequiredMixin, ListView):
    model = User
    form_class = NewAccountForm
    template_name = 'aplicatieTicketing/user_form.html'
    # context_object_name = 'users'

    def get_context_data(self, *args, **kwargs):
        data = super(ViewAccountList, self).get_context_data(*args, **kwargs)
        if self.request.user.is_superuser:
            data['all_users'] = User.objects.all()
        else:
            data['all_users'] = User.objects.filter(id=self.request.user.id)
        return data


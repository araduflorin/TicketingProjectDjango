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


    def get_success_url(self):
        return reverse('aplicatieTicketing:login')

# class ListofUsersList(LoginRequiredMixin, ListView):
#     model = User
#     form_class = NewAccountForm
#     template_name = 'aplicatieTicketing/user_form.html'
#     context_object_name = 'users'

    # def get_context_data(self, *args, **kwargs):
    #     data = super(ListofUsersList, self).get_context_data(*args, **kwargs)
    #     if self.request.user.is_superuser:
    #         data['all_users'] = User.objects.all()
    #     else:
    #         data['all_users'] = User.objects.filter(id=self.request.user.id)
    #     return data
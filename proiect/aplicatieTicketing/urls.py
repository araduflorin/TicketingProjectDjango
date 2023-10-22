from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

from aplicatieTicketing import views

app_name = 'aplicatieTicketing'

urlpatterns = [
    path('', views.general, name='generalHtml'),
    # path('adaugare/', views.CreateRegistrationView.as_view(), name='adaugare'),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='generalHtml'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('contact/', views.CreateContactView.as_view(), name='contact'),
    path('contact_list/', views.ViewContact.as_view(), name='contact_list'),
    path('success/', views.success, name='success'),
    # path('user_list/', views.all_users, name='lista_utilizatori'),
    path('user_list/', views.ListofUsersList.as_view(), name='lista_utilizatori'),
    path('ticket/', views.CreateTicket.as_view(), name='ticket'),
    path('ticket_list/', views.ViewTicket.as_view(), name='ticket_list'),
    path('type_ticket/', views.CreateTypeTicket.as_view(), name='type_ticket'),
    path('type_list/', views.ViewTypeTicket.as_view(), name='type_list'),
    path('<int:pk>/modify_type/', views.UpdateTypeTicket.as_view(), name='modify_type'),
    path('status_ticket/', views.CreateStatusTicket.as_view(), name='status_ticket'),
    path('status_list/', views.ViewStatusTicket.as_view(), name='status_list'),



]
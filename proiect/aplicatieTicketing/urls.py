from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

from aplicatieTicketing import views

app_name = 'aplicatieTicketing'

urlpatterns = [
    path('', views.general, name='generalHtml'),
    path('accounts/', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('login/', views.login_user, name='login'),
    path('contact/', views.CreateContactView.as_view(), name='contact'),
    path('contact_list/', views.ViewContact.as_view(), name='contact_list'),
    path('success/', views.success, name='success'),
    path('ticket/', views.CreateTicket.as_view(), name='ticket'),
    # path('ticket_admin/', views.CreateTicketAdmin.as_view(), name='ticket_admin'),
    path('ticket_list/', views.ViewTicket.as_view(), name='ticket_list'),
    path('ticket_view/', views.ListTicket.as_view(), name='ticket_view'),
    path('ticket_inter/', views.InterPageTicket.as_view(), name='ticket_inter'),
    path('<int:pk>/modify_ticket/', views.UpdateTicket.as_view(), name='modify_ticket'),
    path('<int:pk>/modify_ticket_admin/', views.UpdateTicketAdmin.as_view(), name='modify_ticket_admin'),
    path('type_ticket/', views.CreateTypeTicket.as_view(), name='type_ticket'),
    path('type_list/', views.ViewTypeTicket.as_view(), name='type_list'),
    path('<int:pk>/modify_type/', views.UpdateTypeTicket.as_view(), name='modify_type'),
    path('<int:pk>/delete_type/', views.delete_type, name='delete_type'),
    path('status_ticket/', views.CreateStatusTicket.as_view(), name='status_ticket'),
    path('status_list/', views.ViewStatusTicket.as_view(), name='status_list'),
    path('<int:pk>/modify_status/', views.UpdateStatusTicket.as_view(), name='modify_status'),
    path('<int:pk>/delete_status/', views.delete_status, name='delete_status'),

]
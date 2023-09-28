from django.contrib.auth.views import LoginView
from django.urls import path, include

from aplicatieTicketing import views

app_name = 'aplicatieTicketing'

urlpatterns = [
    path('', views.general, name='generalHtml'),
    path('adaugare/', views.CreateRegistrationView.as_view(), name='adaugare'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('contact/', views.CreateContactView.as_view(), name='contact'),

]
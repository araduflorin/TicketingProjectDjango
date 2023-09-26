from django.urls import path, include

from aplicatieTicketing import views

app_name = 'aplicatieTicketing'

urlpatterns = [
    path('aplicatieTicketing/', views.general, name='general'),
    path('adaugare/', views.CreateRegistrationView.as_view(), name='adaugare'),


]
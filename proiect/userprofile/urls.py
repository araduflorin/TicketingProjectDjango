from django.urls import path

from userprofile import views

app_name='username'

urlpatterns = [
    path('new_account/', views.CreateNewAccountView.as_view(), name='new_user'),
]
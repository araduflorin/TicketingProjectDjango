from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('userprofile/', views.CreateNewAccountView.as_view(), name='new_user'),

]
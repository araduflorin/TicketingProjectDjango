from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('userprofile/', views.CreateNewAccountView.as_view(), name='new_user'),
    path('<int:pk>/edit_user/', views.UpdateAccountView.as_view(), name='edit_user'),
    path('user_list/', views.ViewAccountList.as_view(), name='lista_utilizatori'),
]
from django.db import models
from phone_field import PhoneField


# Create your models here.
class Registration(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    id_user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    telephone = PhoneField(blank=True, help_text='Phone number')


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id_user}" \
               f"{self.password}{self.confirm_password}{self.email}{self.telephone}"

from django import forms
from django.db import models
from django.shortcuts import render
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


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    telephone = PhoneField(blank=True, help_text='Phone number')
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}{self.email}{self.telephone}{self.message}"


class Ticket(models.Model):
    subject_ticket = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    telephone = PhoneField(blank=True, help_text='Phone number')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_ticket}{self.status}{self.type}{self.name}{self.email}{self.telephone}"



class Status(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}{self.description}"

class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}{self.description}"

class TicketType(models.Model):

    type_name = models.CharField(max_length=30)
    type_description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_name}{self.type_description}"


from django import forms
from django.db import models
from django.shortcuts import render
from phone_field import PhoneField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}{self.email}{self.message}"


class Ticket(models.Model):

    st1 = 'stare1'
    st2 = 'stare2'
    st3 = 'stare3'
    stare = [(st1, 'Inchis'), (st2, 'Confirmat'),(st3, 'Respins'),]
    subject_ticket = models.CharField(max_length=30)
    status = models.CharField(max_length=15, choices=Status.name)
    type = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_ticket}{Status(self.status)}{self.type}{self.name}{self.email}"


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




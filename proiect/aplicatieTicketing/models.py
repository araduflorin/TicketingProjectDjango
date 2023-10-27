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


class Ticket(models.Model):
    subject_ticket = models.CharField(max_length=30)
    # status = models.CharField(max_length=15)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    # type = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_ticket}{Status.name}{self.type}{self.name}{self.email}"







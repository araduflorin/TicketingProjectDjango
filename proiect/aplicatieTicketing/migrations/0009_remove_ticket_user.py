# Generated by Django 4.2.5 on 2023-10-19 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatieTicketing', '0008_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
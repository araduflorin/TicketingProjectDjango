# Generated by Django 4.2.5 on 2023-10-10 11:41

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatieTicketing', '0003_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_ticket', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=40)),
                ('telephone', phone_field.models.PhoneField(blank=True, help_text='Phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30)),
                ('type_description', models.CharField(max_length=100)),
            ],
        ),
    ]

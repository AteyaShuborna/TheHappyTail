# Generated by Django 4.1.7 on 2023-04-23 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_customuser_auth_token_customuser_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='auth_token',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
    ]

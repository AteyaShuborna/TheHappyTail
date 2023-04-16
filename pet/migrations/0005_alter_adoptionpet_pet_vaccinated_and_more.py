# Generated by Django 4.1.7 on 2023-04-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_alter_adoptionpet_user_alter_missingpet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionpet',
            name='pet_vaccinated',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='missingpet',
            name='pet_vaccinated',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

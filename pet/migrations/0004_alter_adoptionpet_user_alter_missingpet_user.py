# Generated by Django 4.1.7 on 2023-04-16 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_customuser_id_alter_customuser_email'),
        ('pet', '0003_adoptionpet_pet_age_missingpet_pet_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionpet',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
        migrations.AlterField(
            model_name='missingpet',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
    ]

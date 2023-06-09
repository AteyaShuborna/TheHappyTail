# Generated by Django 4.1.7 on 2023-04-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_adoptionrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missinginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='adoptionrequest',
            name='can_pick_up',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='adoptionrequest',
            name='had_pet',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

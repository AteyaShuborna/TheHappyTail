# Generated by Django 4.1.7 on 2023-05-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_missinginfo_alter_adoptionrequest_can_pick_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionpost',
            name='pet_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adoptionpost',
            name='pet_gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adoptionpost',
            name='pet_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='missingpost',
            name='pet_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='missingpost',
            name='pet_gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='missingpost',
            name='pet_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

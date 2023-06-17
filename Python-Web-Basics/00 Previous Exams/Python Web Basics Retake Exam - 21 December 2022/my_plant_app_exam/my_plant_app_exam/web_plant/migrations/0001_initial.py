# Generated by Django 4.2.2 on 2023-06-09 18:43

import django.core.validators
from django.db import migrations, models
import my_plant_app_exam.web_plant.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), my_plant_app_exam.web_plant.validators.only_letters_validator])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[my_plant_app_exam.web_plant.validators.upper_case_validator])),
                ('last_name', models.CharField(max_length=20, validators=[my_plant_app_exam.web_plant.validators.upper_case_validator])),
            ],
        ),
    ]
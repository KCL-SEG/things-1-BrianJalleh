# Generated by Django 4.1.2 on 2022-10-14 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(30)])),
                ('description', models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(120)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]

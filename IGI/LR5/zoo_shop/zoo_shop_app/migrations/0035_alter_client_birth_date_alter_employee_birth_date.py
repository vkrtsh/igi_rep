# Generated by Django 5.0.4 on 2024-10-21 22:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_shop_app', '0034_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.DateField(null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2006, 10, 27), message='You must be at least 18 years old to register')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2006, 10, 27), message='You must be at least 18 years old to register')]),
        ),
    ]
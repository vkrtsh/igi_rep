# Generated by Django 5.0.4 on 2024-05-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_shop_app', '0018_client_birth_date_client_photo_client_user_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
    ]
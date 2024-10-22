# Generated by Django 5.0.4 on 2024-10-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_shop_app', '0032_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutshop',
            name='image',
            field=models.ImageField(upload_to='static/main/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default='static/main/user.png', upload_to='static/clients/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='static/main/user.png', upload_to='employees/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='static/main/news.png', upload_to='static/news/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/main/empty.jpg', upload_to='static/products/'),
        ),
    ]

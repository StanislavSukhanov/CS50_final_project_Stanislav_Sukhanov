# Generated by Django 2.0.2 on 2018-03-04 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chocs', '0014_productinbasket_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='image',
        ),
    ]

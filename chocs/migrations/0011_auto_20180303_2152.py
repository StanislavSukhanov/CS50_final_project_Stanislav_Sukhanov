# Generated by Django 2.0.2 on 2018-03-03 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chocs', '0010_productinbasket_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='quantity',
            new_name='number',
        ),
    ]

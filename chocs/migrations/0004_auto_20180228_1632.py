# Generated by Django 2.0.2 on 2018-02-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocs', '0003_auto_20180228_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='candies_images/%Y/%M/%D'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sets_images'),
        ),
    ]
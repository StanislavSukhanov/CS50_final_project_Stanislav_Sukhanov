# Generated by Django 2.0.2 on 2018-02-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter a name of a candy', max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='candies_images/%D/%m/%Y')),
                ('description', models.TextField(help_text='Enter a brief description of an item', max_length=1000)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('can_update_models', 'Can update models'),),
            },
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name of an item', max_length=40)),
                ('summary', models.TextField(help_text='Enter a brief description of an item', max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sets_images/%Y/%m/%D')),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('d', 'Under development'), ('o', 'Out of stock'), ('i', 'In production')], default='d', help_text='Item availability', max_length=1)),
                ('candy_item', models.ManyToManyField(help_text='Select a candy for this set', to='chocs.Candy')),
            ],
        ),
        migrations.DeleteModel(
            name='Chocs',
        ),
    ]
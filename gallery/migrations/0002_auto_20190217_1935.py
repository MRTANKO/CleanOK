# Generated by Django 2.0.4 on 2019-02-17 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фотографию', 'verbose_name_plural': 'Фотографии'},
        ),
    ]

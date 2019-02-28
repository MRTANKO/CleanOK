# Generated by Django 2.0.4 on 2019-02-18 05:05

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20190217_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(max_length=30, validators=[services.models.Request.validate_phone], verbose_name='Телефон'),
        ),
    ]

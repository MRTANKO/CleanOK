# Generated by Django 2.0.4 on 2019-02-23 09:00

from django.db import migrations, models
import vacancy.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_auto_20190219_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(validators=[vacancy.models.Vacancy.validate_salary], verbose_name='Зарплата'),
        ),
    ]

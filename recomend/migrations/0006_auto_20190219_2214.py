# Generated by Django 2.0.4 on 2019-02-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomend', '0005_auto_20190211_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomend',
            name='usl',
            field=models.ImageField(upload_to='Recomend', verbose_name='Фотография сертификата'),
        ),
    ]
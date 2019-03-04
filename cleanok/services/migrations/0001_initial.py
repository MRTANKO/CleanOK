# Generated by Django 2.0.4 on 2019-03-04 06:28

from django.db import migrations, models
import django.db.models.deletion
import services.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название пункта работы')),
            ],
            options={
                'verbose_name': 'Пункт работы',
                'verbose_name_plural': 'Пункты работы',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, validators=[services.validators.validate_phone], verbose_name='Телефон')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название услуги')),
                ('desc', models.TextField(verbose_name='Комментарий к услуге')),
                ('price', models.IntegerField(validators=[services.validators.validate_price], verbose_name='Минимальная цена')),
                ('note', models.TextField(verbose_name='Примечание')),
                ('warn', models.TextField(verbose_name='Предупреждение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Category', verbose_name='Категория услуги')),
                ('items', models.ManyToManyField(related_name='items_service', to='services.Item', verbose_name='Пункты работы')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service', verbose_name='Услуга'),
        ),
    ]

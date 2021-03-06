# Generated by Django 3.0.8 on 2021-02-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Código promocional')),
                ('discount', models.FloatField(default=0.0, verbose_name='Descuento')),
                ('valid_from', models.DateTimeField(verbose_name='Válido de')),
                ('valid_to', models.DateTimeField(verbose_name='Válido hasta')),
                ('used', models.BooleanField(default=False, verbose_name='Usado')),
            ],
            options={
                'verbose_name': 'Código promocional',
                'verbose_name_plural': 'Códigos promocionales',
                'ordering': ['code'],
            },
        ),
    ]

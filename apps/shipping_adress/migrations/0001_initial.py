# Generated by Django 3.0.8 on 2021-01-15 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=50, verbose_name='Carrera')),
                ('line2', models.CharField(max_length=50, verbose_name='Calle')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('state', models.CharField(max_length=50, verbose_name='Departamento')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
                ('reference', models.CharField(max_length=150, verbose_name='Referencia')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Código postal')),
                ('cellphone', models.CharField(max_length=12, verbose_name='Número telefónico')),
                ('default', models.BooleanField(default=False, verbose_name='Por defecto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dirección de envio',
                'verbose_name_plural': 'Direcciones de envio',
                'ordering': ['default', 'created_at'],
            },
        ),
    ]
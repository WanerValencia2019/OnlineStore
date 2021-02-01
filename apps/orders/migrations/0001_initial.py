# Generated by Django 3.0.8 on 2021-02-01 21:10

import apps.orders.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping_adress', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing_profiles', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=150, unique=True)),
                ('status', models.CharField(choices=[(apps.orders.models.OrderStatus['CREATED'], 'CREATED'), (apps.orders.models.OrderStatus['PAYED'], 'PAYED'), (apps.orders.models.OrderStatus['COMPLETED'], 'COMPLETED'), (apps.orders.models.OrderStatus['CANCELED'], 'CANCELED')], default=apps.orders.models.OrderStatus['CREATED'], max_length=50)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=5500.0, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_profiles.BillingProfiles')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('shipping_adress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_adress.ShippingAdress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Orden de compra',
                'verbose_name_plural': 'Orden de compras',
                'db_table': '',
                'managed': True,
            },
        ),
    ]

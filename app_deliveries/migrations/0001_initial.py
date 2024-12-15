# Generated by Django 5.1.3 on 2024-12-09 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_branch', '0001_initial'),
        ('app_company', '0001_initial'),
        ('app_products', '0001_initial'),
        ('app_users', '0004_alter_usermodel_first_name_alter_usermodel_last_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price_per_item', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_products.productsmodel', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('order_status', models.CharField(choices=[('pending_for_courier', 'Pending for a Courier'), ('pending_for_restaurant', 'Pending for a Restaurant'), ('confirmed_by_restaurant', 'Confirmed by a Restaurant'), ('delivering', 'Delivering'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending_for_courier', max_length=25, verbose_name='Order Status')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='app_branch.branchmodel', verbose_name='Branch')),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_delivering', to=settings.AUTH_USER_MODEL, verbose_name='Courier')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_users.userlocations', verbose_name='Delivery Address')),
                ('order_items', models.ManyToManyField(related_name='orders', to='app_deliveries.orderitemmodel', verbose_name='Order Items')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='app_company.restaurantmodel', verbose_name='Restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_orders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-11 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to='customer.customer')),
                ('pizza_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_id', to='customer.menu')),
            ],
        ),
    ]

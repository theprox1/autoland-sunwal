# Generated by Django 3.1.3 on 2020-11-27 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20201127_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.customer'),
        ),
    ]

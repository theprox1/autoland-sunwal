# Generated by Django 3.1.3 on 2020-11-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_auto_20201127_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_booked',
            field=models.DateField(auto_now_add=True),
        ),
    ]

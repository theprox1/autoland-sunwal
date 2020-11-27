# Generated by Django 3.1.3 on 2020-11-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='car',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='carname',
        ),
        migrations.AddField(
            model_name='book',
            name='carname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='complete',
            field=models.BooleanField(max_length=200, null=True),
        ),
    ]
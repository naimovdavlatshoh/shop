# Generated by Django 3.2.6 on 2022-04-03 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 9, 31, 20, 330532, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]
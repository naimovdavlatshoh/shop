# Generated by Django 4.0.1 on 2022-04-19 13:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0025_remove_favourite_is_favourite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 13, 48, 33, 806739, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='recomendation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='recomendation')),
            ],
            options={
                'verbose_name': 'Recomendation',
                'verbose_name_plural': 'Recomendations',
            },
        ),
    ]

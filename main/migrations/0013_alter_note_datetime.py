# Generated by Django 3.2.6 on 2023-01-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20230128_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

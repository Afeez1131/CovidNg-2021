# Generated by Django 3.0.5 on 2021-01-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0008_total_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='total',
            options={'ordering': ('day',)},
        ),
        migrations.AlterField(
            model_name='total',
            name='day',
            field=models.IntegerField(max_length=200),
        ),
    ]

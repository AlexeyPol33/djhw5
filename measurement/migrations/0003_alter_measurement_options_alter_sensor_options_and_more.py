# Generated by Django 4.1.5 on 2023-03-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Сенсор'},
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

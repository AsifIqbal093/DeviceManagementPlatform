# Generated by Django 4.1.12 on 2023-11-29 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_telemetrydata_temperature_alter_telemetrydata_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telemetrydata',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices_data', to='devices.devicesinfo'),
        ),
    ]

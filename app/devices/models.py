# models.py

from django.db import models
from django.conf import settings


class DevicesInfo(models.Model):
    """
    Represents information about a device.

    Fields:
    - device_name (CharField): The name of the device.
    - description (TextField): A description of the device.
    - owner (ForeignKey): The owner of the device.

    Methods:
    - __str__(): Returns a string representation of the device name.
    """

    device_name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='devices',
        default=None,
        unique=False
    )

    def __str__(self):
        """
        Returns a string representation of the device name.

        Returns:
        - str: The device name.
        """
        return self.device_name


class TelemetryData(models.Model):
    """
    Model representing telemetry data from devices.
    """

    # Foreign key relationship with DevicesInfo model
    device = models.ForeignKey(
        DevicesInfo,
        on_delete=models.CASCADE,
        related_name='devices_data',
        unique=False
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    temperature = models.FloatField()

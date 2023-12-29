# serializers.py

from rest_framework import serializers
from .models import DevicesInfo, TelemetryData


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevicesInfo
        fields = '__all__'
        read_only_fields = ['owner']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if user.role == 'Owner':
            data['owner'] = user.id
        return data


class TelemetryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetryData
        fields = '__all__'

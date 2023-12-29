from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import DevicesInfo, TelemetryData


class DevicesInfoModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            name='Test User',
            role='lev_manager'  # Adjust the role as needed for your test case
        )
        self.device = DevicesInfo.objects.create(
            device_name='Test Device',
            description='Test Description',
            owner=self.user
        )

    def test_device_info_creation(self):
        device = DevicesInfo.objects.get(device_name='Test Device')
        self.assertEqual(device.device_name, 'Test Device')
        self.assertEqual(device.description, 'Test Description')
        self.assertEqual(device.owner, self.user)

    def test_device_info_str(self):
        device = DevicesInfo.objects.get(device_name='Test Device')
        self.assertEqual(str(device), 'Test Device')


class TelemetryDataModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User',
            role='lev_operator'
        )
        self.device_info = DevicesInfo.objects.create(
            device_name='Test Device',
            description='Test Description',
            owner=self.user
        )

    def test_telemetry_data_model(self):
        telemetry_data = TelemetryData.objects.create(
            device=self.device_info,
            status='OK',
            temperature=25.5
        )

        self.assertEqual(telemetry_data.device, self.device_info)
        self.assertEqual(telemetry_data.status, 'OK')
        self.assertEqual(telemetry_data.temperature, 25.5)

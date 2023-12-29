from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate, APIRequestFactory

from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.urls import reverse

from devices.models import DevicesInfo
from devices.views import DevicesListView, DevicesDetailView


class DevicesListViewTest(APITestCase):
    def setUp(self):
        self.owner_user = get_user_model().objects.create(
            name='owner_user',
            email='owner_user@test.com',
            password='testpassword',
            role='owner'
        )
        self.engineer_user = get_user_model().objects.create(
            name='engineer_user',
            email='engineer_user@test.com',
            password='testpassword',
            role='lev_engineer'
        )
        self.operator_user = get_user_model().objects.create(
            name='operator_user',
            email='operator_user@test.com',
            password='testpassword',
            role='lev_operator'
        )
        self.manager_user = get_user_model().objects.create(
            name='manager_user',
            email='manager_user@test.com',
            password='testpassword',
            role='lev_manager'
        )

    def test_returns_all_devices_for_lev_roles(self):
        DevicesInfo.objects.create(
            device_name='Device 1',
            description='Device 1 description',
            owner=self.owner_user
        )
        DevicesInfo.objects.create(
            device_name='Device 2',
            description='Device 2 description',
            owner=self.owner_user
        )
        request = RequestFactory().get('/devices_list/')
        force_authenticate(request, user=self.engineer_user)
        view = DevicesListView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), DevicesInfo.objects.count())

    def test_returns_owned_devices_for_owner_role(self):

        device1 = DevicesInfo.objects.create(
            device_name='Device 1',
            description='Description 1',
            owner=self.owner_user
        )
        device2 = DevicesInfo.objects.create(
            device_name='Device 2',
            description='Description 2',
            owner=self.owner_user
        )
        request = RequestFactory().get('/devices_list/')
        force_authenticate(request, user=self.owner_user)
        view = DevicesListView.as_view()

        # Act
        response = view(request)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['device_name'], device1.device_name)
        self.assertEqual(response.data[1]['device_name'], device2.device_name)

    def test_creates_new_device_for_owner_role_with_valid_data(self):

        data = {'device_name': 'New Device', 'description': 'New Description'}
        request = RequestFactory().post('/devices_list/', data=data)
        force_authenticate(request, user=self.owner_user)
        view = DevicesListView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(DevicesInfo.objects.count(), 1)
        self.assertEqual(DevicesInfo.objects.first().device_name, 'New Device')

    def test_returns_empty_list_for_owner_role_with_no_devices(self):

        request = RequestFactory().get('/devices/')
        force_authenticate(request, user=self.owner_user)
        view = DevicesListView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_returns_400_error_if_request_data_is_invalid(self):

        data = {'device_name': '', 'description': 'New Description'}
        request = RequestFactory().post('/devices_list/', data=data)
        force_authenticate(request, user=self.owner_user)
        view = DevicesListView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 400)


class DevicesDetailViewTest(APITestCase):
    def setUp(self):
        self.owner_user = get_user_model().objects.create(
            name='owner_user',
            email='owner_user@test.com',
            password='testpassword',
            role='owner'
        )

    def test_retrieve_device_owned_by_user(self):

        device = DevicesInfo.objects.create(
            device_name='Device 1',
            description='Device 1 description',
            owner=self.owner_user
        )
        request = RequestFactory().get('/device/1')
        force_authenticate(request, user=self.owner_user)
        view = DevicesDetailView.as_view()

        response = view(request, pk=device.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['device_name'], 'Device 1')
        self.assertEqual(response.data['description'], 'Device 1 description')
        self.assertEqual(response.data['owner'], self.owner_user.id)

    def test_update_device_owned_by_user(self):

        device = DevicesInfo.objects.create(
            device_name='Device 1',
            description='Device 1 description',
            owner=self.owner_user
        )
        data = {
            'device_name': 'Updated Device',
            'description': 'Updated description'
        }
        url = reverse('device-detail', kwargs={'pk': device.pk})
        request = APIRequestFactory().put(url, data, format='json')
        force_authenticate(request, user=self.owner_user)
        view = DevicesDetailView.as_view()

        response = view(request, pk=device.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['device_name'], 'Updated Device')
        self.assertEqual(response.data['description'], 'Updated description')
        self.assertEqual(response.data['owner'], self.owner_user.id)

    def test_delete_device_owned_by_user(self):

        device = DevicesInfo.objects.create(
            device_name='Device 1',
            description='Device 1 description',
            owner=self.owner_user
        )
        request = RequestFactory().delete('/device/1')
        force_authenticate(request, user=self.owner_user)
        view = DevicesDetailView.as_view()

        response = view(request, pk=device.pk)
        self.assertEqual(response.status_code, 204)

    def test_return_403_when_user_not_authenticated(self):

        request = RequestFactory().get('/devices/1')
        view = DevicesDetailView.as_view()

        response = view(request, pk=1)
        self.assertEqual(response.status_code, 401)

    def test_return_404_when_device_not_owned_by_user(self):

        user2 = get_user_model().objects.create(
            name='owner_user2',
            email='owner_user2@test.com',
            password='testpassword',
            role='owner'
        )
        device = DevicesInfo.objects.create(
            device_name='Device 1',
            description='Device 1 description',
            owner=self.owner_user
        )
        request = RequestFactory().get('/device/1')
        force_authenticate(request, user=user2)
        view = DevicesDetailView.as_view()
        response = view(request, pk=device.pk)
        self.assertEqual(response.status_code, 404)

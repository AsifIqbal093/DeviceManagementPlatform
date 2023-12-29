# urls.py

from django.urls import path
from .views import DevicesListView, DevicesDetailView

urlpatterns = [
    path('devices_list/', DevicesListView.as_view(), name='devices-list'),
    path(
        'device/<int:pk>/',
        DevicesDetailView.as_view(),
        name='device-detail'
    ),
]

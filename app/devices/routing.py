from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/influxdb_reader/$', consumers.InfluxDBConsumer.as_asgi()),
]

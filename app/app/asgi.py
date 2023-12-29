"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""


# asgi.py
import os
# from django.urls import re_path as url

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from channels.routing import ProtocolTypeRouter, URLRouter  # noqa
from django.core.asgi import get_asgi_application  # noqa
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack  # noqa
import devices.routing  # noqa

# Import get_asgi_application after setting DJANGO_SETTINGS_MODULE
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            devices.routing.websocket_urlpatterns
        )
    ),
})

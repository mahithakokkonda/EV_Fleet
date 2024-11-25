"""
ASGI config for ev_fleet_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ev_fleet_management.settings")

application = get_asgi_application()
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ev_fleet_management.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Add other protocols like WebSocket here if needed
})

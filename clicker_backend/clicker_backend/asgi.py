import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator 
from clicker_app.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack
import clicker_app.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": application,
    'websocket': 
        URLRouter(
            clicker_app.routing.websocket_urlpatterns
        )
})
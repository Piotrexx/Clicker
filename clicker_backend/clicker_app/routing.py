from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ship/', consumers.ClickConsumers.as_asgi(), name="clicker")
]
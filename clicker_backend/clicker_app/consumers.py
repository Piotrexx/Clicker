from .models import Ship, Planet
from channels.generic.websocket import AsyncWebsocketConsumer, StopConsumer
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
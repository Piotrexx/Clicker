from .models import User, Planet
from channels.generic.websocket import AsyncWebsocketConsumer, StopConsumer
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
import json

class ClickConsumers(AsyncWebsocketConsumer):
    
    user = None

    async def connect(self):
        if self.scope['subprotocols'][0] is None:
            await self.close()

        token = self.scope['subprotocols'][0]
        validated_token = await database_sync_to_async(JWTAuthentication().get_validated_token)(token)
        self.user = await database_sync_to_async(JWTAuthentication().get_user)(validated_token)
        
        if self.user.is_authenticated:
            await self.accept()
            return self.send("Connected to space!")
        
        return self.close()
    
    async def receive(self, text_data=None, bytes_data=None):
        return await self.save_click()
    
    async def save_click(self):
        self.user.score += (1 * self.user.ship_upgrade)
        self.user.asave()
        return self.user.score
    
    

        

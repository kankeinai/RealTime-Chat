from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import ChatRoom, Message 
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class ChatRoomConsumer(AsyncWebsocketConsumer):
    
    @database_sync_to_async
    def get_chat(self):
        self.q = ChatRoom.objects.filter(room_name=self.room_name)[0]
    
    @database_sync_to_async
    def save_message(self, message, username):
        user = User.objects.get(username=username)
        Message.objects.create(chatroom = self.q, author = user, message = message).save()
        

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.get_chat()
        
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
        await self.accept()
        
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        
        await self.save_message(message, username)

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )
        
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
        
    pass
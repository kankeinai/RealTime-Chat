from django.db import models
from django.utils import timezone

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=200)
    
    
    

class Message(models.Model):
    chatroom = models.ForeignKey('chatapp.ChatRoom', on_delete=models.CASCADE, related_name='chatroom')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    message = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    
    
# Create your models here.

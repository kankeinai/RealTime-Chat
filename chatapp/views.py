from django.core.checks import messages
from django.shortcuts import render
from .models import ChatRoom, Message 

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def room(request, room_name):
    try:
        q = ChatRoom.objects.filter(room_name=room_name)[0]
    except:
        ChatRoom.objects.create(room_name = room_name).save()
        
    q = ChatRoom.objects.filter(room_name=room_name)[0]
    messages = Message.objects.filter(chatroom = q)
            
    return render(request, 'chatroom.html',{
        'room_name': room_name,
        'messages': messages,
    })
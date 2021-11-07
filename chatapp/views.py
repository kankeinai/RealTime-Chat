from django.core.checks import messages
from django.shortcuts import render
from .models import ChatRoom, Message 
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def room(request, room_name):
    try:
        ChatRoom.objects.create(room_name = room_name).save()
    except:
        print("Already exists")
        
    q = ChatRoom.objects.filter(room_name=room_name)[0]
    messages = Message.objects.filter(chatroom = q, date__date=timezone.now().date())
    
            
    return render(request, 'chatroom.html',{
        'room_name': room_name,
        'messages': messages,
    })
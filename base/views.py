from django.shortcuts import render
from . models import User,Topic,Room,Message
from django.db.models import Q

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    topics=Topic.objects.all()
    rooms=Room.objects.filter(Q(topic__name__icontains=q) |
                              Q(name__icontains=q)|
                              Q(host__username__icontains=q)) 
    room_messages=Message.objects.filter(room__topic__name__icontains=q)
    context={'topics':topics,'rooms':rooms,'room_messages':room_messages}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    context={'room':room,' room_messages': room_messages}
    return render(request,'base/room.html',context)


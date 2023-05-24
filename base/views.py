from django.shortcuts import render,redirect
from . models import User,Topic,Room,Message
from django.db.models import Q
from . forms import RoomForm

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
    participants=room.participants.all()
    context={'room':room,'room_messages': room_messages,'participants':participants}
    return render(request,'base/room.html',context)

def createRoom(request):
    topics=Topic.objects.all()
    form=RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home')
    context={'topics':topics,'form':form}
    return render(request,'base/create-room.html',context)

def updateRoom(request,pk):
    topics=Topic.objects.all()
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method == 'POST':
       topic_name=request.POST.get('topic')
       topic,created=Topic.objects.get_or_create(name=topic_name)
       form=RoomForm(request.POST,instance=room)
       room.name=request.POST.get('name')
       room.topic=topic
       room.description=request.POST.get('description')
       room.save()
       return redirect('home')
       
    context={'room':room,'topics':topics,'form':form}
    return render(request,'base/create-room.html',context)

def uesrProfile(request,pk):
    user=User.objects.get(id=pk)
    topics=Topic.objects.all()
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    context={'topics':topics,'rooms':rooms,'room_messages':room_messages,'user':user}
    return render(request,'base/profile.html',context)



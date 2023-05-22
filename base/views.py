from django.shortcuts import render
from . models import User,Topic,Room,Message

def home(request):
    q=request.Get.get('q') if request.GET.get('q')!=None else ''
    topics=Topic.objects.all()
    rooms=Room.objects.filter(topic__name__icontains=q)
    context={'topics':topics,'rooms':rooms}
    return render(request,'base/home.html',context)




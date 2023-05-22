from django.shortcuts import render
from . models import User,Topic,Room,Message

def home(request):
    topics=Topic.objects.all()
    context={'topics':topics}
    return render(request,'base/home.html',context)




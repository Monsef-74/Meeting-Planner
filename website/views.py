from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    return render(request,'website/index.html', 
                  {"meetings": Meeting.objects.all()})

def about(request):
    return HttpResponse('I am Monsef')

def members(request):
    return HttpResponse('memeber here')

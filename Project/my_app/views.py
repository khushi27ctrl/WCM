from django.shortcuts import render,HttpResponse
from datetime import datetime
from my_app.models import CONTACT

# Create your views here.
def index(request):
    context={'variable1': 'this is sent',
    'variable2': 'khushi mangla'}
    return render(request,'index.html',context)
    # return HttpResponse('this is my home page')
def ABOUT(request):
    return render(request,'ABOUT.html')
    # return HttpResponse('this is about page')   

def CONTACT(request):
    if request.method=="POST":
       email = request.POST.get('email')
       desc = request.POST.get('desc')
       Contact= CONTACT(email=email,desc=desc,date=datetime.today())
       Contact.save()
    return render(request,'CONTACT.html')
    #  return HttpResponse('this is about contact page') 

def WASTAGES(request):
    return render(request,'WASTAGES.html')
    # return HttpResponse('this is about wastages')
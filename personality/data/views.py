from django.shortcuts import render
from contact.models import *
#from contact.forms import *
from django.http import *


def data(request):
    obj = student.objects.all()
    return render (request,'index1.html',{'obj':obj})
# Create your views here.

from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib import messages


def contact(request):
    if request.method == 'POST':

        form = details_forms(request.POST)
        if form.is_valid():
           form.save()
           form = details_forms()
           messages.success(request,'Details Sent Successfully')
        return render(request,'contact.html',{'form':form})
    else:
        form = details_forms()
    return render(request,'contact.html',{'form':form})


def data(request):
    obj = student.objects.all()
    return render(request,'index1.html',{'obj':obj})
















# def contact(request):
#     if request.method == 'POST':
#
#         form = details_forms(request.POST)
#
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         phone = request.POST.get('phone', '')
#         message = request.POST.get('message', '')
#         details_obj = student(name=name,email=email,phone=phone,message=message)
#         details_obj.save()
#         form = details_forms()
#
#
#
#     else:
#         form = details_forms()
#     return render(request,'contact.html',{'form':form})

















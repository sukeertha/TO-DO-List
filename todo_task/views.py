from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import taskes

# Create your views here.

def add_task(request):
    add_task = request.POST['add_task'] # to print the tasks that is typed by user
    taskes.objects.create(task=add_task) # to store the add_task in databse
    return redirect('home')

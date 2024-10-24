from django.http import HttpResponse
from django.shortcuts import render
from todo_task.models import taskes
def home(request):
    # return HttpResponse('<h1>Home page</h1>')
    task = taskes.objects.filter(is_completed=False)
    completed_task = taskes.objects.filter(is_completed=True)
    context = { 'task':task, 'completed_task':completed_task }
    return render(request,'home.html',context)

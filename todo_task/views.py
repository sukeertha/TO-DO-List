from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from . models import taskes

# Create your views here.

def add_task(request):
    add_task = request.POST['add_task'] # to print the tasks that is typed by user
    taskes.objects.create(task=add_task) # to store the add_task in databse
    return redirect('home')

def mark_as_done(request,pk):
    task= get_object_or_404(taskes,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task= get_object_or_404(taskes,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit(request,pk):
    get_task= get_object_or_404(taskes,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['add_task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {'get_task':get_task}
        return render(request,'edit.html',context)

def delete(request,pk):
    task = get_object_or_404(taskes,pk=pk)
    task.delete()
    return redirect('home')

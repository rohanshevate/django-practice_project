from django.shortcuts import *
from .models import Tasks
from .forms import  *

# Create your views here.
def index(request):
    car = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': car, 'form':form}
    print(car)
    return render(request, "tasks/list.html", context=context)

# def update(request,pk):
#     task = Tasks.objects.get(id=pk)
#     form = TaskForm(instance=task)
#     if request.method == 'POST':
#         form = TaskForm(request.POST,instance=task)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     context = {'task': task, 'form':form}
#     return render(request, "tasks/update_tasks.html", context=context)

def delete(request,pk):
    task = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")   
    context = {'task':task}     
    return render(request, "tasks/delete.html", context=context)

from django.shortcuts import get_object_or_404, redirect


# def delete(request, pk):
#     # Fetch the task instance to be deleted
#     task = get_object_or_404(Tasks, id=pk)
    
#     # Check if the request method is POST
#     if request.method == 'POST':
#         task.delete()
#         return redirect('/')
    
#     # Render a confirmation page if the method is GET
#     return render(request, 'tasks/delete.html', {'task': task})



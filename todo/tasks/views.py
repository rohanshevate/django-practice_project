from django.shortcuts import *
from .models import Tasks
from .forms import  *

# Create your views here.
def index(request):
    cars = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': cars, 'form':form}
    print(cars)
    return render(request, "tasks/list.html", context=context)

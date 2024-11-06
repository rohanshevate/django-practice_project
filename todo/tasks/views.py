from django.shortcuts import *
from .models import Tasks

# Create your views here.
def index(request):
    cars = Tasks.objects.all()
    context = {'tasks' : cars}
    print(cars)
    return render(request,"tasks/list.html", context=context)

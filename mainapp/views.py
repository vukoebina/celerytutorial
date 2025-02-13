from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, "mainapp/index.html")

from django.shortcuts import render
from .tasks import dummy_and_slow # new
import time # new

def index(request):
    return render(request, "mainapp/index.html")

def dummy_and_slow_view(request): # new
    start_time = time.time()
    dummy_and_slow()
    end_time = time.time()
    execution_time = end_time - start_time
    context = {"task_name": "Dummy and slow", "execution_time": round(execution_time, 2)}
    return render(request, "mainapp/generic.html", context=context)
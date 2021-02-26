from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
# Create your views here.

def index(request):
    # ls = ToDoList.objects.get(id=id)
    return render(request, "index.html")




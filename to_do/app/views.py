from django.shortcuts import render
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import todo
from django.http import HttpResponseRedirect


def index(request):
    todo_items = todo.objects.all().order_by("-added_date")
    return render(request,'index.html',{"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj=todo.objects.create(added_date=current_date,text=content)  #this is use to create database 
    return HttpResponseRedirect("/")
 

@csrf_exempt
def delete_todo(request,todo_id):
    print(todo_id)
    todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

    

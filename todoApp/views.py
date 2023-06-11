from django.shortcuts import render
from django.http import HttpResponse
from todoApp.models import Todo

def index(request):
   #return HttpResponse("<h2>Главная</h2>")
   return render(request, "index.html")

def todoList(request):
  # return HttpResponse("<h2>Список дел</h2>")
  context = {
     'title': 'Список дел',
     'todoList':Todo.objects.all()
  }
  return render(request, "todoList.html", context)

def addTodo(request):
  # return HttpResponse("<h2>Добавлени нового дела</h2>")
   if request.method =="POST":
      textTodo = request.POST.get("textTodo", "ничего!")
      newtask = Todo.objects.create(textTodo=textTodo)
      print(newtask)   
   else:
       return render(request, "addTodo.html")


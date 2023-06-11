from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('todoList', views.todoList),
   path('addTodo', views.addTodo),
]

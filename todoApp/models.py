from django.db import models

class Todo(models.Model):
    textTodo = models.TextField()
    
    def __str__(self):
        return self.textTodo

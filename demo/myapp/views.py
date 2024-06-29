from django.shortcuts import render, HttpResponse
from .models import ToDoItem

# Create your views here.


def home(request):
    # return HttpResponse("Hello World") 
    return render(request, "home.html")    # render the template


# new view to render a template that will view all of the different todo list items that we have
def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", { "todos": items })  # pass objects as a dictionary

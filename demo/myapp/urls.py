# we place here different urls for our app and connect them to views

from django.urls import path
from . import views     # views.py file

urlpatterns = [
    path('', views.home, name="home"),
    path('todos/', views.todos, name="todos")
]



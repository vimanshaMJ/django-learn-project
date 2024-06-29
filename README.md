pip install django
django-admin startproject demo

# _init_.py

A special file that tells python to treat this directory like a python package

# asgi.py & wsgi.py

Special configuration files that we dont deal with. These allow django to communicate with web server

# settings.py

We go here when we need to install different django applications, install plugins, change middlewares and modify database engins

# urls.py

allow us to config different URL routes

# manage.py

Acts as a command line tool
Allow us to run special commands, make migrations, run python server,...

#####

cd .\demo\
python manage.py startapp myapp

link this myapp to our project: go to settings.py -> Installed apps -> add "myapp"

# admin.py

Allow us to register database modals, so we can view them on our admin panel

# models.py

We place our database models

# tests.py

We write some automated tests cases

# views.py

We create different views that we can access on our website

#####

make a view, create a path in urls.py file, create a view for that path in urls.py file in project file (demo)

# html template

Reusable html file that allow us to display dynamic data
-- Create "tamplates" folder inside myapp -> base.html, home.html
-- render the file : views.py

##### DATABASES

models.py -> create a database model that we can access and use from django
Django provides an ORM - Object Relational Mapping
-> We can create python code to create database model and it automatically made for us a structured database schema

# models.py -> admin.py

Register different models here
Now make migrations (anytime if you changed the database model, you have to make migrations). It will update database for you
-- python manage.py makemigrations
-- python manage.py migrate

create "todos.html" for todo list template -> make a new view -> create URL for this template
Go to django admin panel to see those different items

# Django admin panel

Provided by django which allows us to manage users in different database models.
If we want to work with django admin panel, first create a user
-- python manage.py createsuperuser -> username: vimansha, password: 1234
-- run the server -> http://127.0.0.1:8000/admin ->

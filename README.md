# Django
## Create Virtual Environment
conda create --name VenvName PackageName=version(3.5)

## Activate
source activate MyDjangoEnv

## Deactivate
source deactivate

## Django Create project
django-admin startproject first_project

## Structure of django project
* **__init__.py -**  This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
* **settings.py -** This is where you will store all your project settings
* **urls.py -** This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application.
* **wsgi.py -** This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production
* **manage.py -** This is a Python script that we will use a lot. It will be associates with many commands as we build our web app!

## Install Django
conda install django

## Run Server
python manage.py runserver

**Note** - settings.py change DEBUG to false to avoid log message to user

## Create app inside project
python manage.py startapp first_app

## Structure of app
* **__init__.py -**	This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
* **admin.py -** You can register your models here which Django will then use them with Django’s admin interface.
* **apps.py -** Here you can place application specific configurations
* **models.py -** Here you store the application’s data models
* **tests.py -** Here you can store test functions to test your code
* **views.py -** This is where you have functions that handle requests and return responses
* **Migrations folder-** This directory stores database specific information as it relates to the models

**Note** - Inform project about the newly created app by adding app details to settings.py INSATALLED_APPS

## Mapping URLS
    include() function from django.conf.urls (Specific URL for app)
    from django.urls import path, include
    from first_app import views
    urlpatterns = [
        path('app/', include('first_app.urls')),
    ]

## Templates

* Create a Template folder inside project
* Assign URL in settings.py
* Use template with expression in views.py

## Static Files

* Create a static folder inside project
* Assign URL in settings.py

    STATIC_DIR = os.path.join(BASE_DIR,"static")

    STATICFILES_DIRS = [

        STATIC_DIR,

    ]
* Load static files in html

    {% load staticfiles %}
    
    '<link rel="stylesheet" href="{% static "css/mystyle.css" %}"/>'
    '<img src="{% static "images/img.jpg" %}" alt=" Picture "/>'

## Models ### Branch (Model)
* To create an actual model, we use a class structure inside of the relevant applications models.py file
* This class object will be a subclass of Django’s built-in class:
    django.db.models.Model

    class Topic(models.Model):
        top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

    class Webpage(models.Model):
        topic = models.ForeignKey('Topic',on_delete=models.CASCADE,)
        name = models.CharField(max_length=264,unique=True)
        url = models.URLField(unique=True)

        def __str__(self):
            return self.name

    class AccessRecord(models.Model):
        name = models.ForeignKey('Webpage',on_delete=models.CASCADE,)

        date = models.DateField()

        def __str__(self):
            return str(self.date)
* Migrate the database
    python manage.py migrate
* Then register the changes to your app, shown here with some generic “app1”:
    python manage.py makemigrations app1
* Then migrate the database one more time:
    python manage.py migrate
* In order to use the more convenient Admin interface with the models however, we need to register them to our application’s admin.py file

    from django.contrib import admin
    from first_app.models import AccessRecord, Topic, Webpage

    admin.site.register(AccessRecord)
    admin.site.register(Topic)
    admin.site.register(Webpage)
* create a “superuser”
    python manage.py createsuperuser


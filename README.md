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

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    my_dict ={'insert_me' : "Hello am from views.py!"}
    return render(request, 'first_app/index.html', context=my_dict)
def home(request):
    return HttpResponse("Welcome to home!")

def showhelp(request):
    # return HttpResponse("Hello World!")
    my_dict ={'insert_me' : "Help Template!"}
    return render(request, 'first_app/help.html', context=my_dict)
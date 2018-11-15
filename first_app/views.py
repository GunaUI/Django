from django.shortcuts import render
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    my_dicts ={'insert_me' : "Hello am from views.py!",'number': 100}
    return render(request, 'first_app/index.html', context=my_dicts)
    
def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'first_app/users.html',{'form':form})

def help(request):
    my_dict ={'insert_me' : "Hello am from views.py!"}
    return render(request, 'first_app/help.html', context=my_dict)
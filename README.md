# Django
## Model Forms 
* The first thing we need to do is create a forms.py file inside the application! 
* After that we call Django’s built in model forms classes (looks very similar to creating models).
    ```
    from django import forms
    from first_app.models import User

    class NewUserForm(forms.ModelForm):
        <!--"""here you can do form validation like below"""
        """name = forms.CharField(validators=[check_for_z])"""	-->
	class Meta():
		model = User
		fields = '__all__'
    ```
* Views.py

    ```
    from django.shortcuts import render
    from first_app.forms import NewUserForm

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
    ```
* Form HTML

    ```
    <form method="POST">
        {{form.as_p}}
        {% csrf_token %}
        <input type="submit" class="btn btn-primary" value="Submit"/>
    </form>
    ```
#### Next Branch : django-relative-url


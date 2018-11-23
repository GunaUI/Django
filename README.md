# Django
## Password Encryption and user defined database in admin
* Make sure auth,admin,contenttypes  are under the INSTALLED_APPS list in settings.py
    ```
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
    ```
* In your virtual environment: 
    > pip install bcrypt
    > pip install django[argon2]

* Add Password hashers
    ```
        PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        ]
    ```
* Add Password Validator rules
    ```
        AUTH_PASSWORD_VALIDATORS = [
            {
                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                'OPTIONS': {'min-length':9}
            },
            {
                'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
            },
        ]
    ```
* Make sure added template Path, static url(admin static files), media url(user related static files)
    ```
        TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

        STATIC_DIR = os.path.join(BASE_DIR,"static")

        MEDIA_DIR = os.path.join(BASE_DIR,"media")
    ```
    ```
        STATIC_URL = '/static/'

        STATICFILES_DIRS = [

            STATIC_DIR,
        ]

        MEDIA_URL = '/media/'
        MEDIA_ROOT = MEDIA_DIR
    ```

* Model - Import admin's user (predefined) class and extend as below with new fields(portfolio_site, profile_pic)
    ```
        from django.db import models
        from django.contrib.auth.models import User

        class UserProfileInfo(models.Model):

            # Create relationship (don't inherit from User!)

            user = models.OneToOneField(User, on_delete=models.CASCADE)

            # Add any additional attributes you want

            portfolio_site = models.URLField(blank=True)

            profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

            def __str__(self):

                # Built-in attribute of django.contrib.auth.models.User !

                return self.user.username
    ```
    > pip install pillow to use this!
    > Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
* Make sure you registered your newly created model in admin.py
    ```
        admin.site.register(UserProfileInfo)
    ```
* Form (forms.py)
    ```
    from django import forms
    from django.contrib.auth.models import User
    from first_app.models import UserProfileInfo

    class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')

    class UserProfileInfo(forms.ModelForm):

        class Meta():
            model = User
            fields = ('portfolio_site', 'profile_pic')
    ```
* After above changes run migration in virtual env
* Registration form
    ```
        <!DOCTYPE html> 
        {% extends 'first_app/base.html'%} 
        {% load staticfiles %}
        {% block body_block %}

        <div class="jumbotron">
            {% if registerd %}
                <h1>Thank you for registering</h1>
            {% else %}
            <h1>Register Here</h1>
            <h3>fill out the form:</h3>
            <form method="post" enctype="multipart/form-data">
                {% csrf_token %}
                {{ user_form.as_p }}
                {{ profile_form.as_p}}
                <input type="submit" name="" value="Register">
            </form>
            {% endif %}
        </div>
        {% endblock%}
    ```
* Save Registration form
    ```
        def register(request):
        registerd=False

        if request.method=='POST':
            user_form=UserForm(data=request.POST)
            profile_form=UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user=user_form.save()

                user.set_password(user.password)
                user.save()

                profile=profile_form.save(commit=False)
                profile.user=user

                if 'profile_pic' in request.FILES:

                    profile.profile_pic=request.FILES['profile_pic']

                profile.save()

                registerd=True

            else:
                print(user_form.errors,profile_form.errors)
        else:
            user_form=UserForm()
            profile_form=UserProfileInfoForm()

        return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registerd':registerd})
    ```
* Login Form
    ```
    {% extends 'first_app/base.html' %}
    {% block body_block %}

    <div class="jumbotron">
    <h1>please login in</h1>
    <form  action="{% url 'first_app:user_login' %}" method="post">
        {% csrf_token %}
        <label for="username">Username:</label>
        <input type="text" name="username" placeholder="Enter username">

        <label for="password">Password:</label>
        <input type="password" name="password" >
        <input type="submit" name="" value="Login">

    </form>
    </div>
    {% endblock %}
    ```
* Submit Login
    ```
        from django.contrib.auth import authenticate,login,logout
        from django.http import HttpResponseRedirect,HttpResponse
        from django.core.urlresolvers import reverse
        from django.contrib.auth.decorators import login_required

        def user_login(request):
            if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')

                user=authenticate(username=username,password=password)

                if user:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return HttpResponse('account not active')
                else:
                    print ('someone failed login')
                    print ('username: {} and password{}'.format(username,password))

                    return HttpResponse('invalid login')
            else:
                return render(request,'first_app/login.html',{})

    ```
#### Next Branch : django-authentication


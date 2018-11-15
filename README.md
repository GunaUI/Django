# Django
## Relative URL
* Add app names and path to URL PATH
    ```
    app_name = 'first_app'

    urlpatterns = [
        path('', views.users, name='users')
    ]
    ```
* After that use link in html.
    ```
    <a href="{% url 'first_app:users' %}">Users Page</a>
    <a href="{% url 'admin:index' %}">Admin Page</a>
    ```
## Template Inheritance
* Base Template
    ```
        {% block body_block %}
            <!--Anything outside of this will be inherited if you extended-->
        {% endblock %}
    ```
* How to use template
    ```
    {% extends "first_app/base.html"%}
        {% block body_block %}
            <h1>Hello this is help.html</h1>
        {% endblock %}
    ```
## Custom Filters
* create a file.py (eg: my_extras.py)
    ```
    from django import template
    register = template.Library()

    @register.filter(name='replaceEmpty')

    def replaceEmpty(value, args):
        """
        This cuts out all the values of the "arg"
        """
        return value.replace(args, '')
    ```
* use customfilter in html file
    1. load filter file before use custom filter
        ```
        {% load my_extras %}
        ```
    2. use filter syntax
        ```
        {{insert_me | replaceEmpty:"from"}}
        ```
#### Next Branch : django-authentication


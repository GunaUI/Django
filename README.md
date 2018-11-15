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
#### Next Branch : django-relative-url


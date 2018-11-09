# Django
## Models 
* To create an actual model, we use a class structure inside of the relevant applications models.py file
* This class object will be a subclass of Django’s built-in class:
    django.db.models.Model
    ```
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
    ```
* Migrate the database
    > python manage.py migrate
* Then register the changes to your app, shown here with some generic “app1”:
    > python manage.py makemigrations app1
* Then migrate the database one more time:
    > python manage.py migrate
* In order to use the more convenient Admin interface with the models however, we need to register them to our application’s admin.py file
    ```
    from django.contrib import admin
    from first_app.models import AccessRecord, Topic, Webpage

    admin.site.register(AccessRecord)
    admin.site.register(Topic)
    admin.site.register(Webpage)
    ```
* Create a “superuser”
    > python manage.py createsuperuser
## Populate dummy data
    > pip install faker

    
    import os 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

    import django
    django.setup()

    #FAKE POP SCRIPT
    import random
    from first_app.models import AccessRecord, Webpage, Topic
    from faker import Faker

    fakegen = Faker()
    topics = ['Search', 'Social', 'MarketPlace','News','Games']

    def add_topic():
        t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
        t.save()
        return t

    def populate(N=5):
        for entry in range(N):
            # get a topic
            top=add_topic()

            #create fake data for entry
            fake_url=fakegen.url()
            fake_date=fakegen.date()
            fake_name=fakegen.company()

            #create new webpage entry
            webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

            acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

    if __name__=='__main__':
        print('populating script')
        populate(20)
        print('populating complete')
#### Next Branch : django-Model


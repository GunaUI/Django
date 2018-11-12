from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage, User
# Register your models here.

admin.site.register(User)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
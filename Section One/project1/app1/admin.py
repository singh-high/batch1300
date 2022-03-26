from django.contrib import admin

from app1.models import Topic, Webpage, AccessRecord

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django

django.setup()

import random

from app1.models import AccessRecord,Webpage,Topic

from faker import Faker

fake = Faker()

topics = ['Search','Social','Market','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def pop(N):

    for i in range(N):
        top = add_topic()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        AccessRecord.objects.get_or_create(name=webpg,date=fake_date)


if __name__ == '__main__':
    print("Populating")
    pop(30)
    print("completed")
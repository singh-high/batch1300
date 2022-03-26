from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 250, unique = True)

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    name = models.CharField(max_length=250,unique = True)
    url = models.URLField(unique=-True)


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete = models.CASCADE)
    date = models.DateField()

